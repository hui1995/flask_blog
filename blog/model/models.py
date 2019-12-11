from blog import db
from flask_login import UserMixin
from datetime import datetime
class User(UserMixin,db.Model):
    id =db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,nullable=False)
    password_hash=db.Column(db.String(128))
    create_time  = db.Column(db.DateTime, nullable=True,default=datetime.now)



    def __repr__(self):
        return '<User %r>' % self.username
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(32))
    content=db.Column(db.Text,nullable=False)
    cover=db.Column(db.String(1024),nullable=True)
    userid=db.Column(db.Integer)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Integer(32))
    articleid=db.Column(db.Integer(32))
    content=db.Column(db.String(2048),nullable=False)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.content
