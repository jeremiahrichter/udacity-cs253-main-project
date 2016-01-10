import header as h


class Post(h.db.Model):
    subject = h.db.StringProperty(required=True)
    content = h.db.TextProperty(required=True)
    created = h.db.DateTimeProperty(auto_now_add=True)
    last_modified = h.db.DateTimeProperty(auto_now=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return self._render_text
