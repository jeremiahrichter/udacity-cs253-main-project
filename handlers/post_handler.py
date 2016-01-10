import header as h
from header import blog_key
from .handler_class import Handler


class PostHandler(Handler):
    def get(self, post_id):
        key = h.db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = h.db.get(key)
        if post:
            self.render('solo_post.html', post=post)
        else:
            self.error(404)
