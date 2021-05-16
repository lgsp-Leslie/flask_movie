from flask import session, request

from models import AdminOperateLog, AdminLog


# 管理员操作日志
def admin_operate_log(reason):
    obj = AdminOperateLog(
        username=session['admin'],
        ip=request.remote_addr,
        ua=request.user_agent,
        reason=reason,
        admin_id=session['admin_id']
    )
    return obj


# 管理员登录日志
def admin_login_log():
    obj = AdminLog(
        username=session['admin'],
        ip=request.remote_addr,
        ua=request.user_agent,
        admin_id=session['admin_id']
    )
    return obj
