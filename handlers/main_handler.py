from .handler_class import Handler
import header as h
from models.art_model import Art


class MainHandler(Handler):
    def render_front(self, title='', art='', error=''):
        arts = h.db.GqlQuery('select * from Art order by created desc')
        self.render('front.html', title=title, art=art, error=error, arts=arts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')
        if title and art:
            a = Art(title=title, art=art)
            a.put()
            self.redirect('/')
        else:
            error = 'we need both a title and artwork!'
            self.render_front(title=title, art=art, error=error)
