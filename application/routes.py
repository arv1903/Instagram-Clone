from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.models import *
from application.forms import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('protected'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('protected'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return 'This is a protected page. You are logged in as ' + current_user.username

@app.route('/')
def index():
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)