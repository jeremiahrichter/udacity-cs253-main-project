from .handler_class import Handler
from google.appengine.api import memcache


class FlushHandler(Handler):
    def get(self):
        memcache.flush_all()
        self.redirect('/')
