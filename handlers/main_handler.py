from models.post_model import Post
from .handler_class import Handler


class MainHandler(Handler):
    def render_front(self):
        posts = Post.all()
        posts.order('-created')
        self.render('front.html', posts=posts)

    def get(self):
        self.render_front()
