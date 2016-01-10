from .handler_class import Handler
import re
from models.user_model import User

USER_REGEX = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_REGEX = re.compile(r"^[^\s]{8,}$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


class SignupHandler(Handler):
    def valid_username(self, s):
        return USER_REGEX.match(s)

    def valid_password(self, s):
        return PASS_REGEX.match(s)

    def valid_email(self, s):
        return EMAIL_REGEX.match(s)

    def username_in_use(self, username):
        return User.by_name(username)

    def render_page(self, name="", email="", error=""):
        self.render('signup.html', name=name, email=email, error=error)

    def get(self):
        self.render_page()

    def post(self):
        error_msg = ''
        user_name = self.request.get('username')
        user_pass = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        valid_user, valid_pass, valid_email, in_use = (
            self.valid_username(user_name),
            self.valid_password(user_pass),
            self.valid_email(user_email),
            self.username_in_use(user_name)
        )

        if not valid_user:
            error_msg += 'Please enter a 3-20 character username of alphanumeric characters, dashes or underscores.<br>'
        if in_use:
            error_msg += 'Username already in use, choose another.<br>'
        if valid_pass and not (user_pass == user_verify):
            error_msg += 'Both passwords do not match.<br>'
        if not valid_pass:
            error_msg += 'Please enter a password at least 8 characters long.<br>'
        if not valid_email:
            error_msg += 'Please enter a valid email address.<br>'

        if len(error_msg) > 0:
            self.render_page(name=user_name, email=user_email, error=error_msg)
        else:
            user = User.register(name=user_name, password=user_pass,
                                 email=user_email)
            user.put()
            if user:
                self.login(user)
                self.redirect('/welcome')
