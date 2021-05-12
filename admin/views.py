from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from admin.forms import LoginForm
from functools import wraps

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


@admin.route('/logout/', methods=['GET'])
@admin_login_req
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


@admin.route('/edit_password/', methods=['GET', 'POST'])
@admin_login_req
def edit_password():
    return render_template('admin_edit_password.html')


@admin.route('/tag_add/', methods=['GET', 'POST'])
@admin_login_req
def tag_add():
    return render_template('admin_tag_add.html')


@admin.route('/tag_list/', methods=['GET'])
@admin_login_req
def tag_list():
    return render_template('admin_tag_list.html')


@admin.route('/movie_add/', methods=['GET', 'POST'])
@admin_login_req
def movie_add():
    return render_template('admin_movie_add.html')


@admin.route('/movie_list/', methods=['GET'])
@admin_login_req
def movie_list():
    return render_template('admin_movie_list.html')


@admin.route('/preview_add/', methods=['GET', 'POST'])
@admin_login_req
def preview_add():
    return render_template('admin_preview_add.html')


@admin.route('/preview_list/', methods=['GET'])
@admin_login_req
def preview_list():
    return render_template('admin_preview_list.html')


@admin.route('/user_view/', methods=['GET'])
@admin_login_req
def user_view():
    return render_template('admin_user_view.html')


@admin.route('/user_list/', methods=['GET'])
@admin_login_req
def user_list():
    return render_template('admin_user_list.html')


@admin.route('/comment_list/', methods=['GET'])
@admin_login_req
def comment_list():
    return render_template('admin_comment_list.html')


@admin.route('/movie_collect_list/', methods=['GET'])
@admin_login_req
def movie_collect_list():
    return render_template('admin_movie_collect_list.html')


@admin.route('/admin_operate_log_list/', methods=['GET'])
@admin_login_req
def admin_operate_log_list():
    return render_template('admin_operate_log_list.html')


@admin.route('/admin_login_log_list/', methods=['GET'])
@admin_login_req
def admin_login_log_list():
    return render_template('admin_login_log_list.html')


@admin.route('/user_login_log_list/', methods=['GET'])
@admin_login_req
def user_login_log_list():
    return render_template('admin_user_login_log_list.html')


@admin.route('/role_add/', methods=['GET', 'POST'])
@admin_login_req
def role_add():
    return render_template('admin_role_add.html')


@admin.route('/role_list/', methods=['GET'])
@admin_login_req
def role_list():
    return render_template('admin_role_list.html')


@admin.route('/auth_add/', methods=['GET', 'POST'])
@admin_login_req
def auth_add():
    return render_template('admin_auth_add.html')


@admin.route('/auth_list/', methods=['GET'])
@admin_login_req
def auth_list():
    return render_template('admin_auth_list.html')


@admin.route('/admin_add/', methods=['GET', 'POST'])
@admin_login_req
def admin_add():
    return render_template('admin_add.html')


@admin.route('/admin_list/', methods=['GET'])
@admin_login_req
def admin_list():
    return render_template('admin_list.html')
