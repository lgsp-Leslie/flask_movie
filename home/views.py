from flask import Blueprint, render_template, redirect, url_for

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


@home.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('home_register.html')


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

