from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, PasswordField, SelectField, \
    StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, \
    ValidationError, url
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from models import User

class RegisterForm(FlaskForm):
    username = StringField('Your email: ', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
  
    
