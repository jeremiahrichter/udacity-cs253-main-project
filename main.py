#!/usr/bin/env python2

import webapp2
import os
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja2_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class NewPostHandler(Handler):
    def render_newpost(self, subject="", content="", error=""):
        self.render('newpost.html', subject=subject, content=content, error=error)

    def get(self):
        self.render_newpost()

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(subject=subject, content=content)
            p.put()
            self.redirect('/')
        else:
            error = 'You must enter a subject line and some content.'
            self.render_newpost(subject=subject, content=content, error=error)

class MainHandler(Handler):
    def render_front(self):
        posts = Post.all()
        posts.order('-created')
        self.render('front.html', posts=posts)

    def get(self):
        self.render_front()


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newpost', NewPostHandler)
], debug=True)
