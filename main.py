#!/usr/bin/env python2

import webapp2
import os
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Post(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja2_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def render_front(self):
        self.render('front.html')

    def get(self):
        self.render_front()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
