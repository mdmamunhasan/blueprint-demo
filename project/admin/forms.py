from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Length(min=3, max=100)])
    password = PasswordField('Password', [validators.DataRequired()])