from models.post_model import Post
from .handler_class import Handler
import header as h
from header import blog_key
import json as j


class JSONHandler(Handler):
    def get(self, post_id=None):
        json_obj = None

        if post_id:
            key = h.db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = h.db.get(key)
            if post:
                json_obj = self.post_to_dict(post)
        else:

            posts = Post.all().order('-created').run(limit=10)

            if posts:
                json_obj = []
                for post in posts:
                    json_obj.append(self.post_to_dict(post))
        if json_obj:
            self.response.headers.add('Content-Type', 'application/json charset=utf-8')
            self.write(j.dumps(json_obj))

    def post_to_dict(self, post):
        dict_from_post = {
            "content": post.content,
            "subject": post.subject,
            "created": post.created.strftime("%c"),
            "last_modified": post.last_modified.strftime("%c")
        }
        return dict_from_post
