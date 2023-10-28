from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.models import *
from application.forms import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title=f'{current_user.fullname} Profile')

@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/forgot')
def forgot():
    form = ForgotPasswordForm()
    return render_template('forgot_password.html', title='Forgot', form = form)

@app.route('/edit_profile')
def edit_profile():
    form = EditProfileForm()
    return render_template('profile_edit.html', title='Edit Profile', form = form)

@app.route('/reset')
def reset():
    form = ResetPasswordForm()
    return render_template('reset_password.html', title='Reset', form = form)

@app.route('/verif')
def verif():
    form = VerificationResetPasswordForm()
    return render_template('verif.html', title='Verif', form = form)

@app.route('/create_post')
def create():
    form = CreatePostForm()
    return render_template('create_post.html', title='Create', form = form)

@app.route('/edit_post')
def edit_post():
    form = EditPostForm()
    return render_template('edit_post.html', title='Edit Post', form = form)


if __name__ == '__main__':
    app.run(debug=True)