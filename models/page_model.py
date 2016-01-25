import header as h
from handlers.wiki_page_header import markdown_to_html, escape_html


class Page(h.db.Model):
    url = h.db.StringProperty(required=True)
    content = h.db.TextProperty()
    created = h.db.DateTimeProperty(auto_now_add=True)
    last_modified = h.db.DateTimeProperty(auto_now=True)

    @staticmethod
    def parent_key(path):
        return h.db.Key.from_path('/root' + path, 'page')

    @classmethod
    def by_id(cls, page_id, path):
        return cls.get_by_id(page_id, cls.parent_key(path))

    @classmethod
    def all_by_path(cls, path):
        q = cls.all().ancestor(cls.parent_key(path)).order('-created')
        return q

    @classmethod
    def by_url(cls, url):
        p = Page.all().filter('url =', url).get()
        return p

    @classmethod
    def find_page(cls, url):
        p = Page.by_url(url)
        if not p:
            p = Page(url=url, content=h.db.Text(u''), parent=Page.parent_key(url))
        return p

    def update_content(self, content):
        self.content = h.db.Text(escape_html(content))
        self.put()
        return True

    def html(self):
        return markdown_to_html(self.content)
