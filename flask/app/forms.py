from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Pls input username')])
    password = PasswordField('Password', validators=[DataRequired(message='Pls input password')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Login')
    