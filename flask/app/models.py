from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    followed = db.relationship(
        'User',
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref = db.backref('followers', lazy='dynamic'),
        lazy = 'dynamic'
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        # digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/6b541a0a667f5558208aad7309c22936'

    def __repr__(self):
        return '<User: {}>'.format(self.username)
    

followers = db.Table('followers',
    # follower: the user's follower
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    # followed: the user followed whom
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)