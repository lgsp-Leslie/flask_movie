from flask import Flask

from admin.views import admin
from home.views import home

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(home, url_prefix='/')
