from functools import wraps

from flask import session, redirect, url_for, request, abort

from models import Admin, Auth, Role


# 管理员登录装饰器
def admin_login_req(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)

    return decorated_func


# 用户登录装饰器
def user_login_req(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('home.login', next=request.url))
        return func(*args, **kwargs)

    return decorated_func


# 权限控制装饰器
def admin_auth(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        admin_obj = Admin.query.join(
            Role
        ).filter(
            Role.id == Admin.role_id,
            Admin.id == session['admin_id']).first()
        auths = list(map(lambda v: int(v), admin_obj.role.auths.split(',')))
        auth_list = Auth.query.all()
        urls = ['/admin' + v.url for v in auth_list for val in auths if val == v.id]
        urls.append('/admin/')
        rule = request.url_rule
        # print(urls)
        # print(rule)
        if str(rule) not in urls:
            abort(403)
        return func(*args, **kwargs)
    return decorated_func
