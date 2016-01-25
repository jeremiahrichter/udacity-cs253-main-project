from .handler_class import Handler
from models.page_model import Page


class WikiPageHandler(Handler):
    def render_page(self, url, user=None, page=None):
        self.render('display.html', url=url, user=user, page=page)

    def get(self, url):
        page = Page.by_url(url)
        if page:
            self.render_page(url, user=self.user, page=page)
        elif not page and self.user:
            self.redirect('/_edit' + url)
        else:
            self.redirect('/login')
