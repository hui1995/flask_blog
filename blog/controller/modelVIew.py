from flask_admin import Admin

from blog import Article
from blog import app
from blog import db
class BaseModelview(ModelView):
    def getinfo(self):
        return "this is another model"
admin=Admin(app,name='cleanblog',template_mode='bootstrap3')
admin.add_view(BaseModelview(Article, db.session, name=u'文章管理'))