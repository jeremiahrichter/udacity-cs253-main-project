#!/usr/bin/env python2

import webapp2
from handlers.signup_handler import SignupHandler
from handlers.login_handler import LoginHandler
from handlers.logout_handler import LogoutHandler
from handlers.wiki_page_handler import WikiPageHandler
from handlers.edit_page_handler import EditPageHandler

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
app = webapp2.WSGIApplication([
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    (PAGE_RE, WikiPageHandler),
    ('/_edit' + PAGE_RE, EditPageHandler)
], debug=True)
