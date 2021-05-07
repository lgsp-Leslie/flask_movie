from flask import Flask

import conf
from admin.views import admin
from home.views import home
from models import db

app = Flask(__name__)
# 从配置文件加载配置
app.config.from_object(conf.Config)

# 数据库初始化
db.init_app(app)

# 注册蓝图
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(home, url_prefix='/')
