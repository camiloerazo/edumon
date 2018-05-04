from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField


class CommentForm(Form):
    email = EmailField('email')
    password = PasswordField('password')
    
