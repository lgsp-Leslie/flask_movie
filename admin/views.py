from flask import Blueprint, render_template, redirect, url_for

admin = Blueprint('admin', __name__,
                  template_folder='templates',
                  static_folder='../static/admin')


@admin.route('/')
def index():
    return render_template('admin_index.html')


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('admin_login.html')


@admin.route('/logout/', methods=['GET'])
def logout():
    return redirect(url_for('admin.login'))


@admin.route('/edit_password/', methods=['GET', 'POST'])
def edit_password():
    return render_template('admin_edit_password.html')


@admin.route('/tag_add/', methods=['GET', 'POST'])
def tag_add():
    return render_template('admin_tag_add.html')


@admin.route('/tag_list/', methods=['GET'])
def tag_list():
    return render_template('admin_tag_list.html')


@admin.route('/movie_add/', methods=['GET', 'POST'])
def movie_add():
    return render_template('admin_movie_add.html')


@admin.route('/movie_list/', methods=['GET'])
def movie_list():
    return render_template('admin_movie_list.html')


@admin.route('/preview_add/', methods=['GET', 'POST'])
def preview_add():
    return render_template('admin_preview_add.html')


@admin.route('/preview_list/', methods=['GET'])
def preview_list():
    return render_template('admin_preview_list.html')


@admin.route('/user_view/', methods=['GET'])
def user_view():
    return render_template('admin_user_view.html')


@admin.route('/user_list/', methods=['GET'])
def user_list():
    return render_template('admin_user_list.html')


@admin.route('/comment_list/', methods=['GET'])
def comment_list():
    return render_template('admin_comment_list.html')


@admin.route('/movie_collect_list/', methods=['GET'])
def movie_collect_list():
    return render_template('admin_movie_collect_list.html')


@admin.route('/admin_operate_log_list/', methods=['GET'])
def admin_operate_log_list():
    return render_template('admin_operate_log_list.html')


@admin.route('/admin_login_log_list/', methods=['GET'])
def admin_login_log_list():
    return render_template('admin_login_log_list.html')


@admin.route('/user_login_log_list/', methods=['GET'])
def user_login_log_list():
    return render_template('admin_user_login_log_list.html')


@admin.route('/role_add/', methods=['GET', 'POST'])
def role_add():
    return render_template('admin_role_add.html')


@admin.route('/role_list/', methods=['GET'])
def role_list():
    return render_template('admin_role_list.html')


@admin.route('/auth_add/', methods=['GET', 'POST'])
def auth_add():
    return render_template('admin_auth_add.html')


@admin.route('/auth_list/', methods=['GET'])
def auth_list():
    return render_template('admin_auth_list.html')


@admin.route('/admin_add/', methods=['GET', 'POST'])
def admin_add():
    return render_template('admin_add.html')


@admin.route('/admin_list/', methods=['GET'])
def admin_list():
    return render_template('admin_list.html')




