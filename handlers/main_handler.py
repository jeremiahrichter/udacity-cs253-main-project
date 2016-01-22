from .handler_class import Handler
import header as h
from models.art_model import Art
from header import get_coord
from header import gmaps_img

class MainHandler(Handler):
    def render_front(self, title='', art='', error=''):
        arts = h.db.GqlQuery('select * from Art order by created desc')

        arts = list(arts)
        points = filter(None, (a.coords for a in arts))
        img_url = None
        if points:
            img_url = gmaps_img(points)

        self.render('front.html', title=title, art=art,
                    error=error, arts=arts, img_url=img_url)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')
        if title and art:
            a = Art(title=title, art=art, parent=h.art_key())
            coords = get_coord(self.request.remote_addr)
            if coords:
                a.coords = coords
            a.put()
            self.redirect('/')
        else:
            error = 'we need both a title and artwork!'
            self.render_front(title=title, art=art, error=error)
