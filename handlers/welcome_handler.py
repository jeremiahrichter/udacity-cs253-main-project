from .handler_class import Handler


class WelcomeHandler(Handler):
    def get(self):
        if self.user:
            self.write('Welcome, {}!'.format(self.user.username))
        else:
            self.write('No one is logged in.')
