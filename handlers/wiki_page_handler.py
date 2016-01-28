from .handler_class import Handler


class WikiPageHandler(Handler):
    def render_page(self, url, user=None, page=None):
        self.render('display.html', url=url, user=user, page=page)

    def get(self, url):
        if self.page:
            self.render_page(self.url, user=self.user, page=self.page)
        elif not self.page and self.user:
            self.redirect('/_edit' + self.url)
        else:
            self.redirect('/login')
