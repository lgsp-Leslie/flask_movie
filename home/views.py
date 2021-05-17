import uuid

from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from home.forms import RegisterForm
from models import User, db

home = Blueprint('home', __name__,
                 template_folder='templates/',
                 static_folder='../static/home')


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


@home.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('home_login.html')


@home.route('/logout/', methods=['GET'])
def logout():
    return redirect(url_for('home.login'))


# 会员注册
@home.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user_obj = User(username=data['username'], password=generate_password_hash(data['password']), email=data['email'], phone=data['phone'], nickname=data['nickname'], uuid=uuid.uuid4().hex)
        try:
            db.session.add(user_obj)
            db.session.commit()
            flash('注册成功！', 'success')
            return redirect(url_for('home.login'))
        except Exception as e:
            flash('注册失败！', 'danger')

    return render_template('home_register.html', form=form)


@home.route('/member_center/', methods=['GET'])
def member_center():
    return render_template('home_member_center.html')


@home.route('/edit_password/', methods=['GET'])
def edit_password():
    return render_template('home_edit_password.html')


@home.route('/comments/', methods=['GET'])
def comments():
    return render_template('home_comments.html')


@home.route('/login_log/', methods=['GET'])
def login_log():
    return render_template('home_login_log.html')


@home.route('/movie_collect/', methods=['GET'])
def movie_collect():
    return render_template('home_movie_collect.html')

