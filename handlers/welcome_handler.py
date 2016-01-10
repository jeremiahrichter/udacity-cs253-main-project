from .handler_class import Handler


class WelcomeHandler(Handler):
    def render_welcome(self, user=None):
        self.render('welcome.html', user=user)

    def get(self):
        self.render_welcome(self.user)
