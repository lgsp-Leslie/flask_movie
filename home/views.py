import json
import os
import uuid
from io import BytesIO

from flask import Blueprint, render_template, redirect, url_for, flash, make_response, session, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from conf import Config
from home.forms import RegisterForm, LoginForm, UserDetailForm, ModifyPasswordForm, CommentForm
from models import User, db, UserLog, Preview, Tag, Movie, Comment, MovieCollect
from utils.decorator import user_login_req
from utils.filters import change_filename
from utils.utils import get_verify_code, user_login_log

home = Blueprint('home', __name__,
                 template_folder='templates/',
                 static_folder='../static/home')


# 登录验证码
@home.route('/code')
def get_code():
    image, code = get_verify_code()
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = code
    return response


# 首页
@home.route('/<int:page>/', methods=['GET'])
@home.route('/index/<int:page>/', methods=['GET'])
def index(page=1):
    tags = Tag.query.all()
    page_data = Movie.query

    # 标签
    tid = int(request.args.get('tid', 0))
    if tid != 0:
        page_data = page_data.filter_by(tag_id=tid)
    # 星级
    star = int(request.args.get('star', 0))
    if star != 0:
        page_data = page_data.filter_by(star=star)
    # 时间
    time = int(request.args.get('time', 0))
    if time != 0:
        if time == 1:
            page_data = page_data.order_by(Movie.created_at.desc())
        elif time == 2:
            page_data = page_data.order_by(Movie.created_at.asc())

    # 播放量
    pm = int(request.args.get('pm', 0))
    if pm != 0:
        if pm == 1:
            page_data = page_data.order_by(Movie.play_count.desc())
        elif pm == 2:
            page_data = page_data.order_by(Movie.play_count.asc())

    # 评论量
    cm = int(request.args.get('cm', 0))
    if cm != 0:
        if cm == 1:
            page_data = page_data.order_by(Movie.comment_count.desc())
        elif cm == 2:
            page_data = page_data.order_by(Movie.comment_count.asc())

    page_data = page_data.paginate(page=page, per_page=Config.PER_PAGE)

    p = dict(
        tid=tid,
        star=star,
        time=time,
        pm=pm,
        cm=cm
    )

    return render_template('home_index.html', tags=tags, p=p, page_data=page_data)


# 搜索
@home.route('/search/<int:page>', methods=['GET'])
def search(page=1):
    key = request.args.get('key', '')
    movie_obj = Movie.query.filter(Movie.name.ilike('%' + key + '%'))
    movie_count = movie_obj.count()
    page_data = movie_obj.order_by(Movie.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)
    return render_template('home_search.html', key=key, page_data=page_data, movie_count=movie_count)


# 上映预告
@home.route('/animation/', methods=['GET'])
def animation():
    data = Preview.query.all()
    return render_template('home_animation.html', data=data)


# 电影详情
@home.route('/movie_detail/<int:movie_id>/<int:page>/', methods=['GET', 'POST'])
def movie_detail(movie_id=None, page=1):
    movie_obj = Movie.query.get_or_404(int(movie_id))

    form = CommentForm()
    if session['user'] and form.validate_on_submit():
        data = form.data
        comment_obj = Comment(
            content=data['content'],
            movie_id=movie_id,
            user_id=session['user_id'],
        )
        db.session.add(comment_obj)
        movie_obj.comment_count = movie_obj.comment_count + 1
        db.session.add(movie_obj)

        db.session.commit()
        flash('评论成功', 'success')
        return redirect(url_for('home.movie_detail', movie_id=movie_id, page=1))

    movie_obj.play_count = movie_obj.play_count + 1
    db.session.add(movie_obj)
    db.session.commit()

    page_data = Comment.query.filter_by(movie_id=movie_id).order_by(Comment.created_at.desc(),
                                                                    Comment.id.desc()).paginate(page=page,
                                                                                                per_page=Config.PER_PAGE)

    return render_template('home_movie_detail.html', movie_obj=movie_obj, form=form, page_data=page_data)


# 登录
@home.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user_obj = User.query.filter_by(username=data['username']).first()
        if user_obj is None:
            flash('用户不存在', 'danger')
            return render_template('home_login.html', form=form)
        if not user_obj.check_password(data['password']):
            flash('密码错误', 'danger')
            return render_template('home_login.html', form=form)
        if session.get('image').lower() != data['verify_code'].lower():
            flash('验证码错误！', 'danger')
            return render_template('home_login.html', form=form)
        session['user'] = user_obj.username
        session['user_id'] = user_obj.id

        login_type = 'PC'
        user_login_log_obj = user_login_log(login_type)
        db.session.add(user_login_log_obj)
        db.session.commit()
        return redirect(url_for('home.member_center'))
    return render_template('home_login.html', form=form)


# 退出
@home.route('/logout/', methods=['GET'])
@user_login_req
def logout():
    session.pop('user', None)
    session.pop('user_id', None)
    return redirect(url_for('home.login'))


# 会员注册
@home.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user_obj = User(username=data['username'], password=generate_password_hash(data['password']),
                        email=data['email'], phone=data['phone'], nickname=data['nickname'], uuid=uuid.uuid4().hex)
        try:
            db.session.add(user_obj)
            db.session.commit()
            flash('注册成功！', 'success')
            return redirect(url_for('home.login'))
        except Exception as e:
            flash('注册失败！', 'danger')

    return render_template('home_register.html', form=form)


# 个人中心
@home.route('/member_center/', methods=['GET', 'POST'])
@user_login_req
def member_center():
    form = UserDetailForm()
    user_obj = User.query.get(int(session['user_id']))
    form.avatar.validators = []
    if request.method == 'GET':
        form.info.data = user_obj.info

    if form.validate_on_submit():
        data = form.data

        if form.avatar.data.filename != '':
            file_avatar = secure_filename(form.avatar.data.filename)
            # 如果不存在目录，则创建并授权
            if not os.path.exists(Config.UPLOADS_DIR):
                os.makedirs(Config.UPLOADS_DIR)
                os.chmod(Config.UPLOADS_DIR, 6)

            # 格式化名字并保存文件
            avatar = change_filename(file_avatar)
            form.avatar.data.save(Config.UPLOADS_DIR + 'user/avatar/' + avatar)
            user_obj.avatar = avatar

        email_count = User.query.filter_by(email=data['email']).count()
        if data['email'] != user_obj.email and email_count == 1:
            flash('该邮箱已经存在', 'danger')
            return redirect(url_for('home.member_center'))

        phone_count = User.query.filter_by(phone=data['phone']).count()
        if data['phone'] != user_obj.phone and phone_count == 1:
            flash('该手机号码已经存在', 'danger')
            return redirect(url_for('home.member_center'))

        user_obj.username = session['user']
        user_obj.email = data['email']
        user_obj.phone = data['phone']
        user_obj.info = data['username']
        user_obj.nickname = data['nickname']
        db.session.add(user_obj)
        db.session.commit()
        flash('修改成功！', 'success')
        return redirect(url_for('home.member_center'))

    return render_template('home_member_center.html', form=form, user_obj=user_obj)


# 修改密码
@home.route('/edit_password/', methods=['GET', 'POST'])
@user_login_req
def edit_password():
    form = ModifyPasswordForm()
    if form.validate_on_submit():
        user_obj = User.query.filter_by(username=session['user']).first()
        user_obj.password = generate_password_hash(form.pwd.data)
        db.session.add(user_obj)
        db.session.commit()
        flash('密码修改成功,请重新登录', 'success')
        return redirect(url_for('home.logout'))

    return render_template('home_edit_password.html', form=form)


# 评论列表
@home.route('/comments/<int:page>/', methods=['GET'])
@user_login_req
def comments(page=1):
    page_data = Comment.query.filter_by(user_id=session['user_id']).order_by(Comment.created_at.desc(),
                                                                             Comment.id.desc()).paginate(page=page,
                                                                                                         per_page=Config.PER_PAGE)

    return render_template('home_comments.html', page_data=page_data)


# 登录日志
@home.route('/login_log/<int:page>', methods=['GET'])
@user_login_req
def login_log(page=1):
    user_obj = User.query.filter_by(username=session['user']).first()
    page_data = user_obj.user_log_list.order_by(UserLog.created_at.desc()).paginate(page=page, per_page=Config.PER_PAGE)

    return render_template('home_login_log.html', page_data=page_data)


# 电影收藏
@home.route('/movie_collect/<int:page>/', methods=['GET'])
@user_login_req
def movie_collect(page=1):
    page_data = MovieCollect.query.filter_by(user_id=session['user_id']).order_by(MovieCollect.created_at.desc(),
                                                                                  MovieCollect.id.desc()).paginate(
        page=page, per_page=Config.PER_PAGE)
    return render_template('home_movie_collect.html', page_data=page_data)


# 添加电影收藏
@home.route('/movie_add_collect/', methods=['GET'])
@user_login_req
def movie_add_collect():
    data = dict(ok=1)
    u_id = request.args.get('u_id', None)
    m_id = request.args.get('m_id', None)
    if u_id is None or m_id is None:
        data = dict(ok=0)
        return json.dumps(data)

    u_id = int(u_id)
    m_id = int(m_id)

    movie_collect_obj = MovieCollect.query.filter_by(user_id=u_id, movie_id=m_id).count()
    if movie_collect_obj == 1:
        data = dict(ok=0)
    if movie_collect_obj == 0:
        movie_collect_obj = MovieCollect(user_id=u_id, movie_id=m_id)
        db.session.add(movie_collect_obj)
        db.session.commit()
        data = dict(ok=1)
    return json.dumps(data)
