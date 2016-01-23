import header as h
from header import blog_key
from .handler_class import Handler
from .post_header import get_post
import time

class PostHandler(Handler):
    def get(self, post_id):
        post, last_updated = get_post(post_id)
        if post:
            self.render('solo_post.html', post=post,
                        last_updated=(time.time() - last_updated))
        else:
            self.error(404)
