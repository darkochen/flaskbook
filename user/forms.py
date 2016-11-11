from flask_wtf import Form 
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    email = EmailField('Email Address', [
        validators.DataRequired(),
        validators.Email()
        ]
    )
    username = StringField('Username',[
        validators.Required(),
        validators.length(min=4, max=5)
        ]
    )
    password = PasswordField('New Password',[
        validators.Required(),
        validators.EqualTo('confirm', message='Password must match'),
        validators.length(min=4, max=80)
        ]
    )
    confirm = PasswordField('Repeat Password')