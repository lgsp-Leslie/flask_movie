import uuid
from io import BytesIO

from flask import Blueprint, render_template, redirect, url_for, flash, make_response, session
from werkzeug.security import generate_password_hash

from home.forms import RegisterForm, LoginForm
from models import User, db
from utils.decorator import user_login_req
from utils.utils import get_verify_code, user_login_log

home = Blueprint('home', __name__,
                 template_folder='templates/',
                 static_folder='../static/home')


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


@home.route('/')
def index():
    return render_template('home_index.html')


@home.route('/search/', methods=['GET'])
def search():
    return render_template('home_search.html')


@home.route('/animation/', methods=['GET'])
def animation():
    return render_template('home_animation.html')


@home.route('/movie_detail/', methods=['GET'])
def movie_detail():
    return render_template('home_movie_detail.html')


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


@home.route('/member_center/', methods=['GET'])
@user_login_req
def member_center():
    return render_template('home_member_center.html')


@home.route('/edit_password/', methods=['GET'])
@user_login_req
def edit_password():
    return render_template('home_edit_password.html')


@home.route('/comments/', methods=['GET'])
@user_login_req
def comments():
    return render_template('home_comments.html')


@home.route('/login_log/', methods=['GET'])
@user_login_req
def login_log():
    return render_template('home_login_log.html')


@home.route('/movie_collect/', methods=['GET'])
@user_login_req
def movie_collect():
    return render_template('home_movie_collect.html')
