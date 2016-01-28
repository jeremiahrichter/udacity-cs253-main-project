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
        return Page.all_by_path(url).get()

    @classmethod
    def update_content(cls, content, url, v=None):
        safe_content = h.db.Text(escape_html(content))
        if v:
            p = Page.by_id(v, url)
            if p.content != safe_content:
                p.content = safe_content
                p.put()
        else:
            p = Page(url=url, content=h.db.Text(content), parent=Page.parent_key(url))
            p.put()

    def html(self):
        return markdown_to_html(self.content)
