import os

from flask import flash, session
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, validators, ValidationError, FileField, TextAreaField, \
    SelectField, SelectMultipleField, BooleanField

import constants
from models import Admin, Tag


class LoginForm(FlaskForm):
    """ 管理员登录表单 """
    username = StringField(label='用户名', validators=[validators.DataRequired('用户名不能为空'), ], render_kw={
        'class': 'form-control',
        'placeholder': '请输入账号',
        'required': 'required'
    })
    password = PasswordField(label='密码', validators=[validators.DataRequired('密码不能为空'), ], render_kw={
        'class': 'form-control',
        'placeholder': '请输入密码',
        'required': 'required'
    })
    submit = SubmitField(label='登录', render_kw={
        'class': 'btn btn-primary btn-block btn-flat',
    })

    # def validate_username(self, field):
    #     username = field.data
    #     admin = Admin.query.filter_by(username=username).count()
    #     if admin == 0:
    #         flash('账号不存在!', 'danger')
    #         raise ValidationError('账号不存在！')

    def validate(self):
        result = super().validate()
        username = self.username.data
        password = self.password.data
        if result:
            try:
                admin = Admin.query.filter_by(username=username).first()
                if admin is None:
                    flash('账号不存在!', 'danger')
                    result = False
                    self.username.errors = ['账号不存在!']
                elif not admin.check_password(password):
                    flash('密码错误！', 'danger')
                    result = False
                    self.password.errors = ['密码错误!']
            except Exception as e:
                flash('服务器忙，请联系管理员或稍后重试！', 'danger')
                result = False
            return result


class TagForm(FlaskForm):
    name = StringField('标签名称', validators=[validators.DataRequired('标签名不能为空！'),
                                           validators.length(min=1, max=128, message='标签名长度在1-128之间')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入标签名称!',
        'required': 'required'
    })
    submit = SubmitField(label='保存', render_kw={
        'class': 'btn btn-primary',
    })

    def validate_name(self, field):
        name = field.data
        tag = Tag.query.filter_by(name=name).count()
        if tag == 1:
            flash('标签名已存在！', 'danger')
            raise ValidationError('标签名已存在')


class MovieForm(FlaskForm):
    name = StringField(label='片名', validators=[validators.DataRequired('电影名称不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入片名！'
    })
    url = FileField(label='文件', validators=[FileAllowed(constants.UPLOAD_MOVIE_TYPE, '请选择合适的视频类型，仅支持{}'.format(constants.UPLOAD_MOVIE_TYPE))], render_kw={
        'accept': '.mp4, .avi'
    })
    info = TextAreaField(label='简介', validators=[validators.DataRequired('简介不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入简介！',
    })
    logo = FileField(label='封面', validators=[FileAllowed(constants.UPLOAD_IMAGE_TYPE, '请选择合适的图片类型，仅支持{}'.format(constants.UPLOAD_IMAGE_TYPE))], render_kw={
        'accept': '.jpeg, .jpg, .png'
    })
    star = SelectField(label='星级', validators=[validators.DataRequired('请选择星级')], render_kw={
        'class': 'form-control',
    }, coerce=int, choices=[(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')])
    tag_id = SelectField(label='标签', validators=[validators.DataRequired('请选择标签')], render_kw={
        'class': 'form-control',
    }, coerce=int, choices='')
    area = StringField(label='地区', validators=[validators.DataRequired('地区不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入地区！'
    })
    movie_length = StringField(label='电影时长', validators=[validators.DataRequired('电影时长不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入电影时长！'
    })
    release_date = StringField(label='上映日期', validators=[validators.DataRequired('上映日期不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入上映日期！',
        'id': 'input_release_time'
    })
    submit = SubmitField(label='保存', render_kw={
        'class': 'btn btn-primary',
    })


class PreviewForm(FlaskForm):
    name = StringField(label='预告标题', validators=[validators.DataRequired('预告标题不能为空！')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入预告标题！'
    })
    info = TextAreaField(label='预告简介', render_kw={
        'class': 'form-control',
        'placeholder': '电影简介！',
    })
    logo = FileField(label='预告封面', validators=[FileAllowed(constants.UPLOAD_IMAGE_TYPE, '请选择合适的图片类型，仅支持{}'.format(constants.UPLOAD_IMAGE_TYPE))], render_kw={
        'accept': '.jpeg, .jpg, .png'
    })
    submit = SubmitField(label='保存', render_kw={
        'class': 'btn btn-primary',
    })


class ModifyPasswordForm(FlaskForm):
    old_pwd = PasswordField(label='旧密码', validators=[validators.DataRequired('旧密码不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入旧密码！',
    })
    pwd = PasswordField(label='新密码', validators=[validators.DataRequired('新密码不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入新密码！',
    })
    re_pwd = PasswordField(label='确认新密码', validators=[validators.DataRequired('确认新密码不能为空'), validators.EqualTo('pwd', '两次密码不一致')], render_kw={
        'class': 'form-control',
        'placeholder': '请确认新密码！',
    })
    submit = SubmitField(label='修改', render_kw={
        'class': 'btn btn-primary',
    })

    def validate_old_pwd(self, field):
        username = session['admin']
        pwd = field.data
        admin_obj = Admin.query.filter_by(username=username).first()
        if not admin_obj.check_password(pwd):
            raise ValidationError('旧密码错误')


class AuthForm(FlaskForm):
    name = StringField(label='权限名称', validators=[validators.DataRequired('权限名称不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入权限名称！'
    })
    url = StringField(label='权限路径', validators=[validators.DataRequired('权限路径不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入权限路径！'
    })
    submit = SubmitField(label='保存', render_kw={
        'class': 'btn btn-primary',
    })


class RoleForm(FlaskForm):
    name = StringField(label='角色名称', validators=[validators.DataRequired('角色名称不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入角色名称！'
    })
    auths = SelectMultipleField(label='角色权限列表', validators=[validators.DataRequired('角色权限不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请选择角色权限！'
    }, coerce=int, choices='', description='按住Shift或Ctrl再鼠标点击可进行多选操作！')
    submit = SubmitField(label='保存', render_kw={
        'class': 'btn btn-primary',
    })


class AdminForm(FlaskForm):
    username = StringField(label='账号', validators=[validators.DataRequired('账号不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入账号'
    })
    password = PasswordField(label='密码', validators=[validators.DataRequired('密码不能为空')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入密码'
    })
    re_password = PasswordField(label='确认密码', validators=[validators.DataRequired('确认密码不能为空'), validators.EqualTo('password', '两次密码不一样，请确认')], render_kw={
        'class': 'form-control',
        'placeholder': '请输入确认密码'
    })
    role_id = SelectField(label='所属角色', coerce=int, choices='', render_kw={
        'class': 'form-control',
    })
    is_super = BooleanField(label='是否为超级管理员', default=False)
    submit = SubmitField(label='保存', render_kw={
        'class': 'btn btn-primary',
    })

