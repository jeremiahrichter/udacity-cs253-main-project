from .handler_class import Handler


class LogoutHandler(Handler):
    def get(self):
        prev_url = self.request.headers.get('referer', '/')
        self.logout()
        self.redirect(prev_url)
