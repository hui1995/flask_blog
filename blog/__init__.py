from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.model.models import User,Article,Comment
app=Flask(__name__)

app.config.from_object('blog.setting')
# app.config.from_envvar('FLASKER_SETTINGS')
db=SQLAlchemy(app)