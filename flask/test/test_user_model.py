from datetime import datetime, timedelta
import pytest
from app import create_app, db
from app.models import User, Post
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:flask@localhost:3306/flask_blog_db_test?charset=utf8mb4'

class TestUserModel():

    def set_up(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tear_down(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @pytest.fixture(scope='function')
    def env(self):
        yield self.set_up()
        self.tear_down()

    def test_password_hashing(self, env):
        u = User(username='xiaoming')
        u.set_password('xiao')

        assert u.check_password('xiao')
        assert not u.check_password('da')

    # def test_avatar(self):
    #     u = User(username='xiaoming', email='xiaoming@example.com')
    #     assert u.avatar() == 'localhost:8000/api/user-avatar/b582a1e3e4a997d0bcbe2e71e63997e'
        
    def test_follow(self, env):
        u1 = User(username='tommy', email='tommmy@example.com')
        u2 = User(username='linda', email='linda@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        assert u1.followed.all() == []
        assert u2.followed.all() == []
        u1.follow(u2)
        db.session.commit()
        assert u1.is_following(u2)
        assert u1.followed.count() == 1
        assert u1.followed.first().username == 'linda'
        assert u2.followers.count() == 1
        assert u2.followers.first().username == 'tommy'

        u1.unfollow(u2)
        db.session.commit()
        assert not u1.is_following(u2)
        assert u1.followed.count() == 0
        assert u2.followers.count() == 0

    def test_follow_posts(self, env):
        # create four users
        u1 = User(username='tom', email='tom@example.com')
        u2 = User(username='linda', email='linda@example.com')
        u3 = User(username='david', email='david@example.com')
        u4 = User(username='jerry', email='jerry@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body='post from tom', author=u1, timestamp=now+timedelta(seconds=1))
        p2 = Post(body='post from linda', author=u2, timestamp=now+timedelta(seconds=4))
        p3 = Post(body='post from david', author=u3, timestamp=now+timedelta(seconds=3))
        p4 = Post(body='post from jerry', author=u4, timestamp=now+timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        f1 = u1.get_followed_posts().all()
        f2 = u2.get_followed_posts().all()
        f3 = u3.get_followed_posts().all()
        f4 = u4.get_followed_posts().all()

        assert f1 == [p2, p4, p1]
        assert f2 == [p2, p3]
        assert f3 == [p3, p4]
        assert f4 == [p4]

        




