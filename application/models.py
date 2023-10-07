from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id          = db.Column(db.Integer, primary_key = True)
    username    = db.Column(db.String(128), nullable = False)
    password    = db.Column(db.String(128), nullable = False)
    profile_pic = db.Column(db.String(128))
    bio         = db.Column(db.String(128))

class Follower(db.Model):
    __tablename__ = "followers"
    id           = db.Column(db.Integer, primary_key = True)
    id_follower  = db.Column(db.Integer, nullable = False)
    id_following = db.Column(db.Integer, nullable = False)
    status       = db.Column(db.Boolean)

class Post(db.Model):
    __tablename__ = "posts"
    id           = db.Column(db.Integer, primary_key = True)
    author_id    = db.Column(db.String(128), nullable = False)
    photo        = db.Column(db.String(128), nullable = False)
    caption      = db.Column(db.String(128))


class Comment(db.Model):
    __tablename__ = "comments"
    id           = db.Column(db.Integer, primary_key = True)
    text         = db.Column(db.String(1024), nullable = False)
    commenter_id = db.Column(db.Integer, primary_key = True)
    post_id      = db.Column(db.Integer)

class Like(db.Model):
    __tablename__ = "likes"
    id       = db.Column(db.Integer, primary_key = True)
    like_id  = db.Column(db.Integer, nullable = False)
    post_id  = db.Column(db.Integer, nullable = False)
