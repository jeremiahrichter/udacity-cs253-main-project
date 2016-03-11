from webapp2 import RequestHandler
from header import jinja2_env
from .hash import make_secure_val, check_secure_val
from models.user_model import User
from models.page_model import Page


class Handler(RequestHandler):
    user = None
    page = None
    url = None
    v = None

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
        RequestHandler.initialize(self, *args, **kwargs)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
        self.url = self.request.route_args[0] if len(self.request.route_args) > 0 else '/'
        v = self.request.get('v')
        if v and v.isdigit():
            self.v = int(v)
            p = Page.by_id(int(self.v), self.url)
            if p:
                self.page = p
            else:
                self.error(404)
        else:
            self.page = Page.by_url(self.url)
