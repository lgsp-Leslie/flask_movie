from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, ValidationError

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
    name = StringField('标签名称', validators=[validators.DataRequired('标签名不能为空！'), validators.length(min=1, max=128, message='标签名长度在1-128之间')], render_kw={
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
