from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Pls input username')])
    about_me = TextAreaField('About', validators=[Length(min=0, max=140)])
    submit = SubmitField('submit')

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            # search to see if the usernaem already exists in database
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class PostForm(FlaskForm):
    post_content = TextAreaField('Say something', validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')