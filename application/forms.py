from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from application.utils import exists_email, not_exists_email, exists_username
    

class LoginForm(FlaskForm):
    username             = StringField("username", validators=[DataRequired()])
    password             = PasswordField("password", validators=[DataRequired()])
    submit               = SubmitField("login")

class SignUpForm(FlaskForm):
    username             = StringField("username", validators=[DataRequired(), Length(min=4, max=12), exists_username])
    fullname             = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    email                = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    password             = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    confirm_password     = PasswordField("confirm chpassword", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit               = SubmitField("sign up")

class EditProfileForm(FlaskForm):
    username             = StringField("username", validators=[DataRequired(), Length(min=4, max=12), exists_username])
    email                = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    profile_pic          = FileField("profile picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    password             = PasswordField("password", validators=[DataRequired()])
    submit               = SubmitField("update profile")

class ResetPasswordForm(FlaskForm):
    old_password         = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password         = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit               = SubmitField("reset password")

class ForgotPasswordForm(FlaskForm):
    email                = PasswordField("email", validators=[DataRequired(), not_exists_email])
    recaptcha            = RecaptchaField()
    submit               = SubmitField("send link verification to email")

class VerificationResetPasswordForm(FlaskForm):
    password             = PasswordField("new password", validators=[DataRequired(), Length(min = 8)])
    confirm_password     = PasswordField("confirm new password", validators=[DataRequired, Length(min = 8), EqualTo("password")])
    submit               = SubmitField("reset password")


class CreatePostForm(FlaskForm):
    post_pic             = FileField("picture", validators=[DataRequired(), FileAllowed(["jpg", "png", "jpeg"])])
    caption              = TextAreaField("caption")
    submit               = SubmitField("post")

class EditPostForm(FlaskForm):
    caption              = StringField("caption")
    submit               = SubmitField("update post")