from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators


class RegistrationForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=100)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
