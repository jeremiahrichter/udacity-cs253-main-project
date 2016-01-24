from .handler_class import Handler
from models.user_model import User


class LoginHandler(Handler):
    def render_page(self, name="", error=""):
        self.render('login.html', name=name, error=error, user=self.user)

    def get(self):
        self.render_page()

    def post(self):
        user_name = self.request.get('username')
        user_pass = self.request.get('password')

        user = User.login(user_name, user_pass)

        if user:
            self.login(user)
            self.redirect('/')
        else:
            error = 'Either the username or the password wasn\'t valid'
            self.render_page(name=user_name, error=error)
