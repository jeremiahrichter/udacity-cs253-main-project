from .handler_class import Handler
from models.user_model import User


class LoginHandler(Handler):
    def render_page(self, name="", error="", prev_url='/'):
        self.render('login.html', name=name, error=error,
                    user=self.user, prev_url=prev_url)

    def get(self):
        prev_url = self.request.headers.get('referer', '/')
        self.render_page(prev_url=prev_url)

    def post(self):
        prev_url = str(self.request.get('prev_url'))
        if not prev_url or prev_url.startswith('/login'):
            prev_url = '/'
        user_name = self.request.get('username')
        user_pass = self.request.get('password')

        user = User.login(user_name, user_pass)

        if user:
            self.login(user)
            self.redirect(prev_url)
        else:
            error = 'Either the username or the password wasn\'t valid'
            self.render_page(name=user_name, error=error)
