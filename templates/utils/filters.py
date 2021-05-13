import os
import uuid
from datetime import datetime
from functools import wraps

from flask import session, redirect, url_for, request


def admin_login_req(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)

    return decorated_function


# 修改上传文件名称
def change_filename(filename):
    file_info = os.path.splitext(filename)
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + file_info[-1]
    return filename
