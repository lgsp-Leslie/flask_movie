import os


class Config:
    """ 项目配置文件 """

    # 数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask_movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_MAX_OVERFLOW = True

    # FLASK-WTF表单
    SECRET_KEY = 'LGSP_SECRET_KEY'
    WTF_CSRF_SECRET_KEY = 'LGSP_WTF_CSRF_SECRET_KEY'

    # 文件上传根目录
    UPLOADS_DIR = os.path.join(os.path.abspath(os.path.dirname('__file__')), 'static/uploads/')

    # 分页，每页数据的大小
    PER_PAGE = 5
