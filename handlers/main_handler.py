from .handler_class import Handler
from .post_header import top_ten
import time


class MainHandler(Handler):
    def render_front(self):
        posts, last_updated = top_ten()
        self.render('front.html', posts=posts, user=self.user,
                    last_updated=(time.time() - last_updated))

    def get(self):
        self.render_front()
