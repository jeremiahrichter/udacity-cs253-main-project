#!/usr/bin/env python2

import webapp2
import os
import jinja2
from hash import hash_str, check_secure_val, make_secure_val
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja2_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visits_cookie_str = self.request.cookies.get('visits', 0)
        if visits_cookie_str:
            cookie_val = check_secure_val(visits_cookie_str)
            if cookie_val:
                visits = int(cookie_val)
        visits += 1
        new_cookie_val = make_secure_val(str(visits))

        self.response.headers.add_header('Set-Cookie', 'visits={}'.format(new_cookie_val))
        if visits > 10:
            self.write('You are the best ever!')
        else:
            self.write("You've been here {} times".format(visits))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
