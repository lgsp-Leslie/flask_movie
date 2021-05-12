from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, ValidationError

from models import Admin


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
            admin = Admin.query.filter_by(username=username).first()
            if admin is None:
                flash('账号不存在!', 'danger')
                result = False
                self.username.errors = ['账号不存在!']
            elif not admin.check_password(password):
                flash('密码错误！', 'danger')
                result = False
                self.password.errors = ['密码错误!']
            return result

