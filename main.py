#!/usr/bin/env python2

import webapp2
import os
import jinja2
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
        visits = self.request.cookies.get('visits', 0)
        if visits.isdigit():
            visits = int(visits) + 1
        else:
            visits = 0

        self.response.headers.add_header('Set-Cookie', 'visits={}'.format(visits))

        self.write("You've been here {} times".format(visits))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
