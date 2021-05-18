from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, validators, SubmitField, ValidationError, TextAreaField, FileField
from wtforms.fields.html5 import EmailField

import constants
from models import User


class RegisterForm(FlaskForm):
    username = StringField(label='用户名', validators=[validators.DataRequired('用户名不能为空'),
                                                    validators.Length(min=6, max=32, message='用户名长度6-32位')], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入账号',
    })
    password = PasswordField(label='密码', validators=[validators.DataRequired('密码不能为空'),
                                                     validators.Length(min=6, max=18, message='密码长度6-18位')], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码',
    })
    re_password = PasswordField(label='确认密码', validators=[validators.DataRequired('确认密码不能为空'),
                                                          validators.EqualTo('password', '两次密码不一致！')], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入确认密码',
    })
    nickname = StringField(label='昵称', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入昵称',
    })
    email = EmailField(label='邮箱', validators=[validators.DataRequired('邮箱不能为空'), ], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入邮箱',
    })
    phone = StringField(label='手机号码', validators=[validators.DataRequired('手机号码不能为空'),
                                                  validators.Regexp(
                                                      '^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$',
                                                      message='手机号码格式不正确！')],
                        render_kw={
                            'class': 'form-control input-lg',
                            'placeholder': '请输入手机号码'
                        })
    submit = SubmitField(label='注册', render_kw={
        'class': 'btn btn-lg btn-success btn-block',
    })

    def validate_username(self, field):
        username = field.data
        user_obj = User.query.filter_by(username=username).count()
        if user_obj != 0:
            raise ValidationError('用户名已存在')
        return field

    def validate_email(self, field):
        email = field.data
        user_obj = User.query.filter_by(email=email).count()
        if user_obj != 0:
            raise ValidationError('邮箱已存在')
        return field

    def validate_phone(self, field):
        phone = field.data
        user_obj = User.query.filter_by(phone=phone).count()
        if user_obj != 0:
            raise ValidationError('手机号已存在')
        return field


class LoginForm(FlaskForm):
    username = StringField(label='用户名', validators=[validators.DataRequired('用户名不能为空')], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入账号',
    })
    password = PasswordField(label='密码', validators=[validators.DataRequired('密码不能为空')], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码',
    })
    verify_code = StringField('验证码', validators=[validators.DataRequired('验证码不能为空')], render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入验证码',
    })
    submit = SubmitField(label='登录', render_kw={
        'class': 'btn btn-lg btn-success btn-block',
    })


class UserDetailForm(FlaskForm):
    username = StringField(label='用户名', render_kw={
        'class': 'form-control',
        'disabled': 'disabled'
    })
    nickname = StringField(label='昵称', render_kw={
        'class': 'form-control',
        'placeholder': '请输入昵称',
    })
    email = EmailField(label='邮箱', render_kw={
        'class': 'form-control',
        'placeholder': '请输入邮箱',
    })
    phone = StringField(label='手机号码', validators=[validators.Regexp(
        '^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$',
        message='手机号码格式不正确！')],
                        render_kw={
                            'class': 'form-control',
                            'placeholder': '请输入手机号码'
                        })
    info = TextAreaField(label='个人简介',
                         render_kw={
                             'class': 'form-control input-lg',
                         })
    avatar = FileField(label='上传头像', validators=[
        FileAllowed(constants.UPLOAD_IMAGE_TYPE, '请选择合适的图片类型，仅支持{}'.format(constants.UPLOAD_IMAGE_TYPE))],
                       render_kw={
                           'class': 'btn',
                           'accept': '.jpeg, .jpg, .png'
                       })
    submit = SubmitField(label='保存修改', render_kw={'class': 'btn btn-success', })
