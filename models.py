from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

import constants

db = SQLAlchemy()


class User(db.Model):
    """ 会员用户 """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户id')
    username = db.Column(db.String(64), nullable=False, comment='用户账号')
    password = db.Column(db.String(256), nullable=False, comment='密码')
    nickname = db.Column(db.String(64), comment='昵称', default='匿名')
    email = db.Column(db.String(128), comment='邮箱')
    phone = db.Column(db.String(16), comment='手机号')
    info = db.Column(db.Text, comment='用户简介')
    status = db.Column(db.Enum(constants.UserStatus), default=constants.UserStatus.USER_ACTIVE, comment='用户状态')
    avatar = db.Column(db.String(256), comment='头像')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='最后登录时间')
    uuid = db.Column(db.String(256), comment='唯一标识符')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username


class UserLog(db.Model):
    """ 会员登录日志 """
    __tablename__ = 'user_log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='日志id')
    username = db.Column(db.String(64), nullable=False, comment='会员用户名')
    ip = db.Column(db.String(64), comment='登录ip')
    login_type = db.Column(db.String(64), comment='账号平台')
    ua = db.Column(db.String(256), comment='user-agent')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='登录时间')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('user_log_list', lazy='dynamic'))

    def __repr__(self):
        return '<UserLog %r>' % self.username


class Tag(db.Model):
    """ 标签 """
    __tablename__ = 'movie_tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='标签id')
    name = db.Column(db.String(128), nullable=False, comment='标签名')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='创建时间')

    def __repr__(self):
        return '<Tag %r>' % self.name


class Movie(db.Model):
    """ 电影 """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='电影id')
    name = db.Column(db.String(255), nullable=False, comment='电影名称')
    url = db.Column(db.String(255), comment='电影链接')
    info = db.Column(db.Text, comment='电影简介')
    logo = db.Column(db.String(255), comment='电影封面')
    area = db.Column(db.String(255), comment='上映地区')
    release_date = db.Column(db.Date, comment='上映日期')
    movie_length = db.Column(db.String(128), comment='电影时长')
    star = db.Column(db.SmallInteger, comment='星级')
    play_count = db.Column(db.BigInteger, comment='播放统计')
    comment_count = db.Column(db.BigInteger, comment='评论统计')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='添加时间')

    tag_id = db.Column(db.Integer, db.ForeignKey('movie_tag.id'))
    tag = db.relationship('Tag', backref=db.backref('movie_list', lazy='dynamic'))

    def __repr__(self):
        return '<Movie %r>' % self.name


class Preview(db.Model):
    """ 电影上映预告 """
    __tablename__ = 'movie_preview'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='电影上映预告id')
    name = db.Column(db.String(255), nullable=False, comment='电影上映预告名称')
    info = db.Column(db.Text, comment='电影上映预告简介')
    logo = db.Column(db.String(255), comment='电影上映预告封面')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='添加时间')

    def __repr__(self):
        return '<Preview %r>' % self.name


class Comment(db.Model):
    """ 评论 """
    __tablename__ = 'movie_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='评论id')
    content = db.Column(db.Text, comment='评论内容')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='添加时间')

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    movie = db.relationship('Movie', backref=db.backref('comment_list', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('comment_list', lazy='dynamic'))

    def __repr__(self):
        return '<Comment %r>' % self.id


class MovieCollect(db.Model):
    """ 电影收藏 """
    __tablename__ = 'movie_collect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='电影收藏id')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='收藏时间')

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    movie = db.relationship('Movie', backref=db.backref('movie_collect_list', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('movie_collect_list', lazy='dynamic'))

    def __repr__(self):
        return '<MovieCollect %r>' % self.id


class Auth(db.Model):
    """ 权限 """
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='权限id')
    name = db.Column(db.String(64), nullable=False, comment='权限名称')
    url = db.Column(db.String(256), nullable=False, comment='权限路径')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='创建时间')

    def __repr__(self):
        return '<Auth %r>' % self.name


class Role(db.Model):
    """ 角色 """
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='角色id')
    name = db.Column(db.String(64), nullable=False, comment='角色名称')
    auths = db.Column(db.String(1024), comment='角色权限列表')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='创建时间')

    def __repr__(self):
        return '<Role %r>' % self.name


class Admin(db.Model):
    """ 管理员用户 """
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='管理员id')
    username = db.Column(db.String(64), nullable=False, comment='管理员账号')
    password = db.Column(db.String(256), nullable=False, comment='密码')
    is_super = db.Column(db.SmallInteger, comment='是否为超级管理员,0代表超级管理员')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='最后登录时间')

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('admin_list', lazy='dynamic'))

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<Admin %r>' % self.username


class AdminLog(db.Model):
    """ 管理员登录日志 """
    __tablename__ = 'admin_log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='日志id')
    username = db.Column(db.String(64), nullable=False, comment='管理员用户名')
    ip = db.Column(db.String(64), comment='登录ip')
    ua = db.Column(db.String(256), comment='user-agent')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='登录时间')

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    admin = db.relationship('Admin', backref=db.backref('admin_log_list', lazy='dynamic'))

    def __repr__(self):
        return '<AdminLog %r>' % self.username


class AdminOperateLog(db.Model):
    """ 管理员操作日志 """
    __tablename__ = 'admin_operate_log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='日志id')
    username = db.Column(db.String(64), nullable=False, comment='管理员用户名')
    ip = db.Column(db.String(64), comment='登录ip')
    ua = db.Column(db.String(256), comment='user-agent')
    reason = db.Column(db.Text, comment='操作原因')
    created_at = db.Column(db.DateTime, index=True, default=datetime.now(), comment='登录时间')

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    admin = db.relationship('Admin', backref=db.backref('admin_operate_log_list', lazy='dynamic'))

    def __repr__(self):
        return '<AdminOperateLog %r>' % self.username
