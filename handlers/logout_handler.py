from .handler_class import Handler


class LogoutHandler(Handler):
    def get(self):
        self.logout()
        self.redirect('/')
