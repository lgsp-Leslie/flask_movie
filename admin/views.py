import os
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename


import constants
from admin.forms import LoginForm, TagForm, MovieForm, PreviewForm, ModifyPasswordForm

from conf import Config
from models import db, Tag, Movie, Preview, User, Comment, MovieCollect, Admin
from templates.utils.filters import change_filename
from templates.utils.decorator import admin_login_req


admin = Blueprint('admin', __name__,
                  template_folder='templates',
                  static_folder='../static/admin')


# 上下文处理器
@admin.context_processor
def tpl_extra():
    data = dict(
        online_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    return data


@admin.route('/')
@admin_login_req
def index():
    return render_template('admin_index.html')


# 登录
@admin.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin_obj = Admin.query.filter_by(username=data['username']).first()
        # if not admin.check_password(data['password']):
        #     flash('密码错误', 'danger')
        #     return redirect(url_for('admin.login'))
        session['admin'] = data['username']
        session['admin_id'] = admin_obj.id
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin_login.html', form=form)


# 退出
@admin.route('/logout/', methods=['GET'])
@admin_login_req
def logout():
    session.pop('admin', None)
    session.pop('admin_id', None)
    return redirect(url_for('admin.login'))


# 修改密码
@admin.route('/edit_password/', methods=['GET', 'POST'])
@admin_login_req
def edit_password():
    form = ModifyPasswordForm()
    if form.validate_on_submit():
        try:
            admin_obj = Admin.query.filter_by(username=session['admin']).first()
            if admin_obj is None:
                flash('登录失效，请重新登录！', 'danger')
                return redirect(url_for('admin.login'))
            admin_obj.password = generate_password_hash(form.pwd.data)
            db.session.add(admin_obj)
            db.session.commit()
            flash('密码修改成功,请重新登录', 'success')
            return redirect(url_for('admin.logout'))
        except Exception as e:
            flash('服务器忙，请联系管理员或稍后重试！', 'danger')
            return redirect(url_for('admin.index'))
    return render_template('admin_edit_password.html', form=form)


# 添加标签
@admin.route('/tag_add/', methods=['GET', 'POST'])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        name = form.name.data
        try:
            tag = Tag(name=name)
            db.session.add(tag)
            db.session.commit()
            flash('添加成功', 'success')
            return redirect(url_for('admin.tag_list', page=1))
        except Exception as e:
            flash('服务器忙，请联系管理员或稍后重试！', 'danger')
            return redirect(url_for('admin.tag_add'))
    return render_template('admin_tag_add.html', form=form)


# 编辑标签
@admin.route('/tag_edit/<int:tag_id>/', methods=['GET', 'POST'])
@admin_login_req
def tag_edit(tag_id):
    form = TagForm()
    tag_obj = Tag.query.get(tag_id)
    if form.validate_on_submit():
        name = form.name.data
        tag_count = Tag.query.filter_by(name=name).count()
        if tag_obj.name != name and tag_count == 1:
            flash('标签已存在', 'warning')
            return redirect(url_for('admin.tag_edit', tag_id=tag_id))
        try:
            tag_obj.name = name
            db.session.add(tag_obj)
            db.session.commit()
            flash('标签修改成功', 'success')
            return redirect(url_for('admin.tag_list', page=1))
        except Exception as e:
            flash('服务器忙，请联系管理员或稍后重试！', 'danger')
            return redirect(url_for('admin.tag_list', page=1))
    return render_template('admin_tag_edit.html', form=form, tag_obj=tag_obj)


# 标签列表
@admin.route('/tag_list/<int:page>/', methods=['GET'])
@admin_login_req
def tag_list(page=1):
    page_data = Tag.query.paginate(page, per_page=Config.PER_PAGE)
    return render_template('admin_tag_list.html', page_data=page_data)


# 删除标签
@admin.route('/tag_del/<int:tag_id>/', methods=['GET'])
@admin_login_req
def tag_del(tag_id):
    tag_obj = Tag.query.filter_by(id=tag_id).first()
    if not tag_obj:
        flash('查询不到标签，请刷新后重试！', 'warning')
        return redirect(url_for('admin.tag_list', page=1))
    else:
        db.session.delete(tag_obj)
        db.session.commit()
        flash('标签：{}，删除成功！'.format(tag_obj.name), 'success')
        return redirect(url_for('admin.tag_list', page=1))


# 添加电影
@admin.route('/movie_add/', methods=['GET', 'POST'])
@admin_login_req
def movie_add():
    form = MovieForm()
    form.tag_id.choices = [(v.id, v.name) for v in Tag.query.all()]
    if form.validate_on_submit():
        data = form.data
        # 重置为安全的文件名
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)

        # 如果不存在目录，则创建并授权
        if not os.path.exists(Config.UPLOADS_DIR):
            os.makedirs(Config.UPLOADS_DIR)
            os.chmod(Config.UPLOADS_DIR, 6)

        # 格式化名字并保存文件
        url = change_filename(file_url)
        logo = change_filename(file_logo)
        form.url.data.save(Config.UPLOADS_DIR + url)
        form.logo.data.save(Config.UPLOADS_DIR + logo)

        movie = Movie(
            name=data['name'],
            url=url,
            info=data['info'],
            logo=logo,
            star=int(data['star']),
            play_count=0,
            comment_count=0,
            tag_id=int(data['tag_id']),
            area=data['area'],
            release_date=data['release_date'],
            movie_length=data['movie_length']
        )
        try:
            db.session.add(movie)
            db.session.commit()
            flash('添加电影成功', 'success')
            return redirect(url_for('admin.movie_list', page=1))
        except Exception as e:
            flash('添加电影失败', 'error')
            print(e)
            print(form.errors)
    return render_template('admin_movie_add.html', form=form)


# 编辑电影
@admin.route('/movie_edit/<int:movie_id>/', methods=['GET', 'POST'])
@admin_login_req
def movie_edit(movie_id):
    form = MovieForm()
    form.tag_id.choices = [(v.id, v.name) for v in Tag.query.all()]

    # form.url.validators = []
    # form.logo.validators = []
    movie_obj = Movie.query.get(movie_id)

    if request.method == 'GET':
        form.info.data = movie_obj.info
        form.tag_id.data = movie_obj.tag_id
        form.star.data = movie_obj.star
    if form.validate_on_submit():
        data = form.data
        try:
            # 如果不存在目录，则创建并授权
            if not os.path.exists(Config.UPLOADS_DIR):
                os.makedirs(Config.UPLOADS_DIR)
                os.chmod(Config.UPLOADS_DIR, 6)

            if form.url.data.filename != '':
                file_url = secure_filename(form.url.data.filename)
                url = change_filename(file_url)
                form.url.data.save(Config.UPLOADS_DIR + url)
                movie_obj.url = url

            if form.logo.data.filename != '':
                file_logo = secure_filename(form.logo.data.filename)
                logo = change_filename(file_logo)
                form.logo.data.save(Config.UPLOADS_DIR + logo)
                movie_obj.logo = logo

            movie_obj.name = data['name']
            movie_obj.info = data['info']
            movie_obj.area = data['area']
            movie_obj.release_date = data['release_date']
            movie_obj.movie_length = data['movie_length']
            movie_obj.star = int(data['star']),
            movie_obj.tag_id = int(data['tag_id'])
            db.session.add(movie_obj)
            db.session.commit()
            flash('电影修改成功', 'success')
            return redirect(url_for('admin.movie_list', page=1))
        except Exception as e:
            flash('服务器忙，请联系管理员或稍后重试！', 'danger')
            return redirect(url_for('admin.movie_list', page=1))
    return render_template('admin_movie_edit.html', form=form, movie_obj=movie_obj)


# 电影列表
@admin.route('/movie_list/<int:page>/', methods=['GET'])
@admin_login_req
def movie_list(page=1):
    page_data = Movie.query.order_by(Movie.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)
    return render_template('admin_movie_list.html', page_data=page_data)


# 删除电影
@admin.route('/movie_del/<int:movie_id>/', methods=['GET'])
@admin_login_req
def movie_del(movie_id):
    movie_obj = Movie.query.filter_by(id=movie_id).first()
    if not movie_obj:
        flash('查询不到电影，请刷新后重试！', 'warning')
        return redirect(url_for('admin.movie_list', page=1))
    else:
        db.session.delete(movie_obj)
        db.session.commit()
        flash('电影：{}，删除成功！'.format(movie_obj.name), 'success')
        return redirect(url_for('admin.movie_list', page=1))


# 添加预告
@admin.route('/preview_add/', methods=['GET', 'POST'])
@admin_login_req
def preview_add():
    form = PreviewForm()
    if form.validate_on_submit():
        data = form.data

        file_logo = secure_filename(data['logo'].filename)
        if not os.path.exists(Config.UPLOADS_DIR):
            os.makedirs(Config.UPLOADS_DIR)
            os.chmod(Config.UPLOADS_DIR, 6)
        logo = change_filename(file_logo)
        form.logo.data.save(Config.UPLOADS_DIR + logo)

        preview_obj = Preview(name=data['name'], info=data['info'], logo=logo)
        try:
            db.session.add(preview_obj)
            db.session.commit()
            flash('电影预告添加成功', 'success')
            return redirect(url_for('admin.preview_list', page=1))
        except Exception as e:
            flash('服务器忙，请联系管理员或稍后再试！', 'danger')
    return render_template('admin_preview_add.html', form=form)


# 预告列表
@admin.route('/preview_list/<int:page>/', methods=['GET'])
@admin_login_req
def preview_list(page=1):
    page_data = Preview.query.order_by(Preview.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)
    return render_template('admin_preview_list.html', page_data=page_data)


# 删除预告
@admin.route('/preview_del/<int:prev_id>/', methods=['GET'])
@admin_login_req
def preview_del(prev_id):
    try:
        preview_obj = Preview.query.filter_by(id=prev_id).first()
        if preview_obj is None:
            flash('预告不存在，请刷新后重试', 'warning')
            return redirect(url_for('admin.preview_list', page=1))
        else:
            db.session.delete(preview_obj)
            db.session.commit()
            flash('预告删除成功', 'success')
            return redirect(url_for('admin.preview_list', page=1))
    except Exception as e:
        flash('服务器正忙，请稍后重试！', 'danger')
        return redirect(url_for('admin.preview_del', prev_id=prev_id))


# 编辑预告
@admin.route('/preview_edit/<int:prev_id>/', methods=['GET', 'POST'])
@admin_login_req
def preview_edit(prev_id):
    form = PreviewForm()
    preview_obj = Preview.query.filter_by(id=prev_id).first()
    if preview_obj is None:
        flash('预告不存在，请刷新后重试', 'warning')
        return redirect(url_for('admin.preview_list', page=1))

    form.info.data = preview_obj.info

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                if not os.path.exists(Config.UPLOADS_DIR):
                    os.makedirs(Config.UPLOADS_DIR)
                    os.chmod(Config.UPLOADS_DIR, 6)
                if form.logo.data.filename != '':
                    file_logo = secure_filename(form.logo.data.filename)
                    logo = change_filename(file_logo)
                    form.logo.data.save(Config.UPLOADS_DIR + logo)
                    preview_obj.logo = logo

                preview_obj.name = form.name.data
                preview_obj.info = form.info.data

                db.session.add(preview_obj)
                db.session.commit()
                flash('预告编辑成功', 'success')
                return redirect(url_for('admin.preview_list', page=1))
            except Exception as e:
                flash('服务器正忙，请稍后重试！', 'danger')
                return redirect(url_for('admin.preview_list', page=1))
    return render_template('admin_preview_edit.html', form=form, preview_obj=preview_obj)


# 用户详情
@admin.route('/user_view/<int:user_id>/', methods=['GET'])
@admin_login_req
def user_view(user_id):
    user_obj = User.query.filter_by(id=user_id).first()
    if user_obj is None:
        flash('用户不存在，请刷新后重试', 'danger')
        return redirect(url_for('admin.user_list', page=1))
    return render_template('admin_user_view.html', user_obj=user_obj)


# 用户列表
@admin.route('/user_list/<int:page>/', methods=['GET'])
@admin_login_req
def user_list(page=1):
    page_data = User.query.order_by(User.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)
    return render_template('admin_user_list.html', page_data=page_data)


# 删除用户
@admin.route('/user_del/<int:user_id>/', methods=['GET'])
@admin_login_req
def user_del(user_id):
    user_obj = User.query.filter_by(id=user_id).first()
    if user_obj is None:
        flash('用户不存在，请刷新后重试', 'danger')
        return redirect(url_for('admin.user_list', page=1))
    try:
        db.session.delete(user_obj)
        db.session.commit()
        flash('用户删除成功', 'success')
        return redirect(url_for('admin.user_list', page=1))
    except Exception as e:
        flash('服务器正忙，稍后重试', 'danger')
        return redirect(url_for('admin.user_list', page=1))


# 禁用用户
@admin.route('/user_disable/<int:user_id>/', methods=['GET'])
@admin_login_req
def user_disable(user_id):
    user_obj = User.query.filter_by(id=user_id).first()
    if user_obj is None:
        flash('用户不存在，请刷新后重试', 'danger')
        return redirect(url_for('admin.user_list', page=1))
    try:
        user_obj.status = constants.UserStatus.USER_IN_ACTIVE
        db.session.add(user_obj)
        db.session.commit()
        flash('用户成功禁用', 'success')
        return redirect(url_for('admin.user_list', page=1))
    except Exception as e:
        flash('服务器正忙，稍后重试', 'danger')
        print(e)
        return redirect(url_for('admin.user_list', page=1))


# 启用用户
@admin.route('/user_enable/<int:user_id>/', methods=['GET'])
@admin_login_req
def user_enable(user_id):
    user_obj = User.query.filter_by(id=user_id).first()
    if user_obj is None:
        flash('用户不存在，请刷新后重试', 'danger')
        return redirect(url_for('admin.user_list', page=1))
    try:
        user_obj.status = constants.UserStatus.USER_ACTIVE
        db.session.add(user_obj)
        db.session.commit()
        flash('用户成功启用', 'success')
        return redirect(url_for('admin.user_list', page=1))
    except Exception as e:
        flash('服务器正忙，稍后重试', 'danger')
        return redirect(url_for('admin.user_list', page=1))


# 评论列表
@admin.route('/comment_list/<int:page>/', methods=['GET'])
@admin_login_req
def comment_list(page=1):
    page_data = Comment.query.order_by(Comment.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)
    return render_template('admin_comment_list.html', page_data=page_data)


# 删除评论
@admin.route('/comment_del/<int:comment_id>/', methods=['GET'])
@admin_login_req
def comment_del(comment_id):
    comment_obj = Comment.query.filter_by(id=comment_id).first()
    if comment_obj is None:
        flash('评论不存在，请刷新后重试', 'danger')
        return redirect(url_for('admin.comment_list', page=1))
    try:
        db.session.delete(comment_obj)
        db.session.commit()
        flash('评论删除成功', 'success')
        return redirect(url_for('admin.comment_list', page=1))
    except Exception as e:
        flash('服务器正忙，稍后重试', 'danger')
        return redirect(url_for('admin.comment_list', page=1))


# 电影收藏列表
@admin.route('/movie_collect_list/<int:page>/', methods=['GET'])
@admin_login_req
def movie_collect_list(page=1):
    page_data = MovieCollect.query.order_by(MovieCollect.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)
    return render_template('admin_movie_collect_list.html', page_data=page_data)


# 删除收藏电影
@admin.route('/movie_collect_del/<int:collect_id>/', methods=['GET'])
@admin_login_req
def movie_collect_del(collect_id):
    movie_collect_obj = MovieCollect.query.filter_by(id=collect_id).first()
    if movie_collect_obj is None:
        flash('收藏电影不存在，请刷新后重试', 'danger')
        return redirect(url_for('admin.movie_collect_list', page=1))
    try:
        db.session.delete(movie_collect_obj)
        db.session.commit()
        flash('收藏电影删除成功', 'success')
        return redirect(url_for('admin.movie_collect_list', page=1))
    except Exception as e:
        flash('服务器正忙，稍后重试', 'danger')
        return redirect(url_for('admin.movie_collect_list', page=1))


# 管理员操作日志
@admin.route('/admin_operate_log_list/', methods=['GET'])
@admin_login_req
def admin_operate_log_list():
    return render_template('admin_operate_log_list.html')


# 管理员登录日志
@admin.route('/admin_login_log_list/', methods=['GET'])
@admin_login_req
def admin_login_log_list():
    return render_template('admin_login_log_list.html')


# 用户登录日志
@admin.route('/user_login_log_list/', methods=['GET'])
@admin_login_req
def user_login_log_list():
    return render_template('admin_user_login_log_list.html')


# 添加角色
@admin.route('/role_add/', methods=['GET', 'POST'])
@admin_login_req
def role_add():
    return render_template('admin_role_add.html')


# 角色列表
@admin.route('/role_list/', methods=['GET'])
@admin_login_req
def role_list():
    return render_template('admin_role_list.html')


# 添加权限
@admin.route('/auth_add/', methods=['GET', 'POST'])
@admin_login_req
def auth_add():
    return render_template('admin_auth_add.html')


# 权限列表
@admin.route('/auth_list/', methods=['GET'])
@admin_login_req
def auth_list():
    return render_template('admin_auth_list.html')


# 添加管理员
@admin.route('/admin_add/', methods=['GET', 'POST'])
@admin_login_req
def admin_add():
    return render_template('admin_add.html')


# 管理员列表
@admin.route('/admin_list/', methods=['GET'])
@admin_login_req
def admin_list():
    return render_template('admin_list.html')
