from functools import wraps

from flask import session, redirect, url_for, request


# 登录装饰器
def admin_login_req(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)

    return decorated_function
