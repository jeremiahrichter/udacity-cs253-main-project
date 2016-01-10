import header as h
from header import jinja2_env
from .hash import make_secure_val, check_secure_val
from models.user_model import User


class Handler(h.webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja2_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie',
                                         '{0}={1}; Path=/'.format(name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie',
                                         'user_id=; Path=/')

    def initialize(self, *args, **kwargs):
        h.webapp2.RequestHandler.initialize(self, *args, **kwargs)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
