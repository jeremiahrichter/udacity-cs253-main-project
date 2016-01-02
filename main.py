#!/usr/bin/env python2
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import rot13
import signup
from header import valid_day, valid_month, valid_year, escape_html

form = """
<head><style type="text/css">
    .error {{
        color: red;
    }}
</style></head>
<form method="post">
	What is your birthday?
	<br>
	<br>
	<label>Month
	    <input type="text" name="month" value="{month}">
    </label>
    <label>Day
	    <input type="text" name="day" value="{day}">
    </label>
	<label>Year
	    <input type="text" name="year" value="{year}">
	</label>
	<div class="error">{error}</div>
	<br>
	<br>
	<input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form.format(**{"error": error,
                                               "month": escape_html(month),
                                               "day": escape_html(day),
                                               "year": escape_html(year)}))

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me.",
                            user_month, user_day, user_year)
        else:
            self.redirect('/thanks')


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks, that's a valid day!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    ('/rot13', rot13.ROT13Handler),
    ('/signin', signup.SignupHandler)
], debug=True)
