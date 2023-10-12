from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, EmailField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min = 4, max = 8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min = 6)])
    submit   = SubmitField("Log Up")

class SignUpForm(FlaskForm):
    username         = StringField("Username", validators=[DataRequired(), Length(min = 4, max = 8)])
    password         = PasswordField("Password", validators=[DataRequired(), Length(min = 8)])
    email            = EmailField("Email", validators=[DataRequired(), Length(min = 8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message = "Password must match!")])
    submit           = SubmitField("Sign Up")

class EditProfile(FlaskForm):
    username         = StringField("Username", validators=[DataRequired(), Length(min = 4, max = 8)])
    new_name         = TextAreaField("Name")
    new_bio          = TextAreaField("New Bio")
    new_profile_pic  = TextAreaField("New Profile Picture")
    submit           = SubmitField("Update Profile")

class CreatePost(FlaskForm):
    post    = TextAreaField("Post")
    caption = TextAreaField("Caption")
    submit  = SubmitField("Create Post")

class EditPost(FlaskForm):
    new_caption = TextAreaField("New Caption")
    submit      = SubmitField("Update Post")
