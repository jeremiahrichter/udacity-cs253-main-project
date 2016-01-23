from .handler_class import Handler
import header as h
from models.art_model import Art
from header import get_coord
from header import gmaps_img
from header import art_key
import logging
from google.appengine.api import memcache


def get_top_ten(update=False):
    key = 'top10'
    arts = memcache.get(key)
    if arts is None or update:
        logging.error("***DB QUERY***")
        arts = Art.all().order('-created').ancestor(art_key()).run(limit=10)
        arts = list(arts)
        memcache.set(key, arts)
    return arts


class MainHandler(Handler):
    def render_front(self, title='', art='', error=''):
        arts = get_top_ten()

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
            get_top_ten(True)
            self.redirect('/')
        else:
            error = 'we need both a title and artwork!'
            self.render_front(title=title, art=art, error=error)
