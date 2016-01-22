from .handler_class import Handler
import header as h
from models.art_model import Art
import urllib2 as u
import json as j

API_KEY = "e122a3095e9d27100d5a059fc091caee41eb32335ef248ebc98014b89eeab3dd"
IP_URL = "http://api.ipinfodb.com/v3/ip-city/?key={0}&ip={1}&format=json"


class MainHandler(Handler):
    def render_front(self, title='', art='', error=''):
        arts = h.db.GqlQuery('select * from Art order by created desc')
        self.render('front.html', title=title, art=art, error=error, arts=arts)

    def get_coord(self, ip):
        url = IP_URL.format(API_KEY, ip)
        content = None
        try:
            content = u.urlopen(url).read()
        except u.exceptions.HTTPError as e:
            print(e.args)
            return
        if content:
            try:
                response = j.loads(content)
                lat, lng = response['latitude'], response['longitude']
                if lat != '0' and lng != '0':
                    return h.db.GeoPt(lat, lng)
                else:
                    return
            except j.JSONDecodeError as e:
                print(e.args)
                return

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
