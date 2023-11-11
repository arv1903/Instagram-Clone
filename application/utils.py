import os
import secrets
from PIL import Image

from flask import current_app

from wtforms.validators import ValidationError

from application import login_manager
from application.models import User



#FORM UTILS
def exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if user:
        raise ValidationError("Email already exists. Please use a different email.")
    
def not_exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if not user:
        raise ValidationError("Email not found.")

def exists_username(form, username):    
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("Username already exists. Please use a different username")
#END OF FORM UTILS


#LOGIN MANAGER UTILS
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#END OF LOGIN MANAGER UTILS

def save_image(form_picture_data, mode):
    random_hex = secrets.token_hex(5)
    _, f_ext = os.path.splitext(form_picture_data.filename)
    if(mode == 1):
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(current_app.root_path, 'static/', 'images/' + picture_fn)
    else:
        picture_fn = 'images/posts/' + random_hex + f_ext
        picture_path = os.path.join(current_app.root_path, 'static/', picture_fn)

    image  = Image.open(form_picture_data)
    # i_width, i_height = image.size()
    # ratio = i_width / 1000
    # output_size = (i_width / ratio, i_height / ratio)
    # image.thumbnail(image)
    image.save(picture_path)

    return picture_fn