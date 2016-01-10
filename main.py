#!/usr/bin/env python2

import header as h
from handlers.main_handler import MainHandler
from handlers.new_post_handler import NewPostHandler
from handlers.post_handler import PostHandler

app = h.webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newpost', NewPostHandler),
    ('/post/(\d+)', PostHandler)
], debug=True)
