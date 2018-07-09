from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Pls input username')])
    password = PasswordField('Password', validators=[DataRequired(message='Pls input password')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Login')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Pls input username')])
    about_me = TextAreaField('About', validators=[Length(min=0, max=140)])
    submit = SubmitField('submit')