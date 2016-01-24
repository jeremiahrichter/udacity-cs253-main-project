from .handler_class import Handler


class WikiPageHandler(Handler):
    def get(self, url):
        self.render('display.html', url=url, user=self.user)
