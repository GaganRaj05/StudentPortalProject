from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,TextAreaField,EmailField
from wtforms.validators import DataRequired,Length

class loginForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=3)])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=4)])
    submit=SubmitField("submit")
    
