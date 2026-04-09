from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    display_name = StringField("显示名称", validators=[DataRequired(message="此字段为必填项")])
    username = StringField("用户名", validators=[DataRequired(message="此字段为必填项")])
    password = PasswordField("密码", validators=[DataRequired(message="此字段为必填项")])
    password2 = PasswordField(
        "重复密码", validators=[DataRequired(message="此字段为必填项"), EqualTo("password", message="两次密码不一致")]
    )
    submit = SubmitField("注册")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "该用户名已被使用，请选择其他用户名。"
            )


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(message="此字段为必填项")])
    password = PasswordField("密码", validators=[DataRequired(message="此字段为必填项")])
    submit = SubmitField("登录")
