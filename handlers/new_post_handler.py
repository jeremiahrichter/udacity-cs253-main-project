from handlers.post_model import Post
from header import blog_key
from .handler_class import Handler


class NewPostHandler(Handler):
    def render_newpost(self, subject="", content="", error=""):
        self.render('newpost.html', subject=subject, content=content, error=error)

    def get(self):
        self.render_newpost()

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent=blog_key(), subject=subject, content=content)
            p.put()
            self.redirect('/post/{}'.format(p.key().id()))
        else:
            error = 'You must enter a subject line and some content.'
            self.render_newpost(subject=subject, content=content, error=error)
