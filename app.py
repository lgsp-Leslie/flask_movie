from flask_script import Manager
from flask import Flask, render_template

import conf
from admin.views import admin
from home.views import home
from models import db, rd

app = Flask(__name__)

# 关闭调试模式
app.debug = False

# 添加一个命令行解析器
manager = Manager(app)

# 从配置文件加载配置
app.config.from_object(conf.Config)

# 数据库初始化
db.init_app(app)
rd.init_app(app)

# 注册蓝图
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(home, url_prefix='/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('home_404.html'), 404


@app.errorhandler(403)
def page_not_found(error):
    return render_template('403.html'), 403
