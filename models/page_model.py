import header as h
from header import page_key


class Page(h.db.Model):
    url = h.db.StringProperty(required=True)
    content = h.db.TextProperty(required=True)
    created = h.db.DateTimeProperty(auto_now_add=True)
    last_modified = h.db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_url(cls, url):
        p = Page.all().filter('url =', url).get()
        return p

    @classmethod
    def insert_url(cls, url, content):
        p = Page.by_url(url)
        if not p:
            p = Page(url=url, content=content, parent=page_key())
            return p

    @classmethod
    def update_content(cls, url, content):
        p = Page.by_url(url)
        if p:
            p.content = content
            p.put()
            return True
