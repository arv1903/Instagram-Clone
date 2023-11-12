from flask import render_template, redirect, url_for, flash, request, make_response, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message

from application import app, mail
from application.models import *
from application.forms import *
from application.utils import save_image

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
            return redirect(url_for('profile', username = current_user.username))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# @app.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', title=f'{current_user.fullname} Profile')

@app.route('/<string:username>')
@login_required
def profile(username):
    posts = current_user.posts
    return render_template('profile.html', title=f'{current_user.fullname} Profile', posts = posts)

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CreatePostForm()

    if form.validate_on_submit():
        post = Post(
            author_id = current_user.id,
            caption = form.caption.data
        )
        post.photo = save_image(form.post_pic.data, 0)
        db.session.add(post)
        db.session.commit()
        flash('Your image has been posted ❤️!', 'success')

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.post_date.desc()).paginate(page=page, per_page=3)
    # posts.reverse()

    return render_template('index.html', title='Home', form = form, posts = posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            password = form.password.data,
            fullname = form.fullname.data,
            email    = form.email.data,
            profile_pic = 'default.jpg'
        )
        db.session.add(user)
        db.session.commit()
        flash(f'You have successfully created account "{user.username}"')

        return redirect(url_for('login'))
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = ForgotPasswordForm()

    if form.validate_on_submit():
        msg = Message("Hello", sender="marvin07ar@gmail.com", recipients=[form.email.data])
        print(form.email.data)
        mail.send(msg)

    return render_template('forgot_password.html', title='Forgot', form = form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    user = User.query.filter_by(id=current_user.id).first()
    tmp1, tmp2 = user.join_date, user.status
    print(user.username)
    if form.validate_on_submit():
        user.username = form.username.data
        user.fullname = form.fullname.data
        user.email    = form.email.data
        user.profile_pic = save_image(form.profile_pic.data, 1)
        if user.profile_pic == None:
            user.profile_pic = "default.png"
        user.bio = form.bio.data
        user.join_date = tmp1
        user.status = tmp2
        db.session.commit()        
        flash('Your profile is successfully updated!')

        return render_template('profile.html', title=f'{current_user.fullname} Profile', posts = current_user.posts)

    return render_template('profile_edit.html', title='Edit Profile', form = form, username=user.username)

@app.route('/reset')
def reset():
    form = ResetPasswordForm()
    return render_template('reset_password.html', title='Reset', form = form)

@app.route('/verif')
def verif():
    form = VerificationResetPasswordForm()
    return render_template('verif.html', title='Verif', form = form)

@app.route('/create_post')
@login_required
def create():
    form = CreatePostForm()
    return render_template('create_post.html', title='Create', form = form)
    
@app.route('/edit_post')
@login_required
def edit_post():
    form = EditPostForm()
    return render_template('edit_post.html', title='Edit Post', form = form)

@app.route('/like/<int:post_id>', methods=['POST'])
@login_required
def like(post_id):
    like = Like.query.filter_by(liked_by = current_user, post_id = post_id).first()
    if not like:
        like = Like(user_id=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
        return make_response(200, jsonify({"status" : True}))
    db.session.delete(like)
    db.session.commit()
    return make_response(200, jsonify({"status" : False}))

if __name__ == '__main__':
    app.run(debug=True)