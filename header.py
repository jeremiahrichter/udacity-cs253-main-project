import webapp2
import os
import jinja2
from google.appengine.ext import db
import urllib2 as u
import json as j

IP_API_KEY = "e122a3095e9d27100d5a059fc091caee41eb32335ef248ebc98014b89eeab3dd"
IP_URL = "http://api.ipinfodb.com/v3/ip-city/?key={0}&ip={1}&format=json"

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


def blog_key(name='default'):
    return db.Key.from_path('blogs', name)


def art_key(name='default'):
    return db.Key.from_path('art', name)


def get_coord(ip):
    url = IP_URL.format(IP_API_KEY, ip)
    content = None
    try:
        content = u.urlopen(url).read()
    except u.exceptions.HTTPError as e:
        print(e.args)
        return
    if content:
        try:
            response = j.loads(content)
            lat, lng = response['latitude'], response['longitude']
            if lat != '0' and lng != '0':
                return db.GeoPt(lat, lng)
            else:
                return
        except j.JSONDecodeError as e:
            print(e.args)
            return
