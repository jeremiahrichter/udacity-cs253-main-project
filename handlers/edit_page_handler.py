from .handler_class import Handler


class EditPageHandler(Handler):
    def get(self, url):
        self.render('display.html', url=url, user=self.user)
