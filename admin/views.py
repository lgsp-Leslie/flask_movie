from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from admin.forms import LoginForm, TagForm
from functools import wraps

from conf import Config
from models import db, Tag

admin = Blueprint('admin', __name__,
                  template_folder='templates',
                  static_folder='../static/admin')


def admin_login_req(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)

    return decorated_function


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
        # admin = Admin.query.filter_by(username=data['username']).first()
        # if not admin.check_password(data['password']):
        #     flash('密码错误', 'danger')
        #     return redirect(url_for('admin.login'))
        session['admin'] = data['username']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin_login.html', form=form)


# 退出
@admin.route('/logout/', methods=['GET'])
@admin_login_req
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


# 修改密码
@admin.route('/edit_password/', methods=['GET', 'POST'])
@admin_login_req
def edit_password():
    return render_template('admin_edit_password.html')


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
            return redirect(url_for('admin.tag_add'))
        except Exception as e:
            flash('服务器忙，请联系管理员或稍后重试！', 'danger')
            return redirect(url_for('admin.tag_add'))
    return render_template('admin_tag_add.html', form=form)


# 编辑标签
@admin.route('/tag_edit/<int:tag_id>', methods=['GET', 'POST'])
@admin_login_req
def tag_edit(tag_id):
    form = TagForm()
    tag_obj = Tag.query.get(tag_id)
    if form.validate_on_submit():
        name = form.name.data
        tag_count = Tag.query.filter_by(name=name).count()
        if tag_obj.name != name and tag_count == 1:
            flash('标签已存在', 'warning')
            return redirect(url_for('admin.tag_edit'))
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
    return render_template('admin_movie_add.html')


# 电影列表
@admin.route('/movie_list/', methods=['GET'])
@admin_login_req
def movie_list():
    return render_template('admin_movie_list.html')


# 添加预告
@admin.route('/preview_add/', methods=['GET', 'POST'])
@admin_login_req
def preview_add():
    return render_template('admin_preview_add.html')


# 预告列表
@admin.route('/preview_list/', methods=['GET'])
@admin_login_req
def preview_list():
    return render_template('admin_preview_list.html')


# 用户详情
@admin.route('/user_view/', methods=['GET'])
@admin_login_req
def user_view():
    return render_template('admin_user_view.html')


# 用户列表
@admin.route('/user_list/', methods=['GET'])
@admin_login_req
def user_list():
    return render_template('admin_user_list.html')


# 评论列表
@admin.route('/comment_list/', methods=['GET'])
@admin_login_req
def comment_list():
    return render_template('admin_comment_list.html')


# 电影收藏列表
@admin.route('/movie_collect_list/', methods=['GET'])
@admin_login_req
def movie_collect_list():
    return render_template('admin_movie_collect_list.html')


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
