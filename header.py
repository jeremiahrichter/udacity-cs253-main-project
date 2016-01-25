import os
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


def users_key(group='default'):
    return db.Key.from_path('users', group)


def page_key(group='default'):
    return db.Key.from_path('page', group)
