from .handler_class import Handler
from models.page_model import Page


class HistoryPageHandler(Handler):
    def render_page(self, url, user=None, pages=None):
        self.render('history.html', url='/_history' + url, user=user, pages=pages,
                    len=len, str=str)

    def get(self, url):
        pages = Page.all_by_path(url)
        if pages:
            self.render_page(url, user=self.user, pages=pages)
        elif not pages and self.user:
            self.redirect('/_edit' + url)
        else:
            self.redirect('/login')
