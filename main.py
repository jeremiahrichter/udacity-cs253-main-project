#!/usr/bin/env python2

import header as h
from handlers.main_handler import MainHandler

app = h.webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
