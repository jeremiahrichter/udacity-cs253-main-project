#!/usr/bin/env python2

import header as h
from handlers.main_handler import MainHandler
from handlers.new_post_handler import NewPostHandler
from handlers.post_handler import PostHandler
from handlers.signup_handler import SignupHandler
from handlers.welcome_handler import WelcomeHandler
from handlers.login_handler import LoginHandler
from handlers.logout_handler import LogoutHandler
from handlers.json_handler import JSONHandler

app = h.webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newpost', NewPostHandler),
    ('/post/(\d+)', PostHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/.json', JSONHandler),
    ('/post/(\d+).json', JSONHandler)
], debug=True)
