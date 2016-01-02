import webapp2
import string
from header import escape_html

form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
    <style type="text/css">
    </style>
</head>
<body>
<form method="post">
    <h1>Enter text to ROT13</h1>
    <br>
    <textarea name="text">{text}</textarea>
    <br>
    <input type="submit">
</form>
</body>
</html>
"""


class SignInHandler(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(form.format(**{"text": text}))

    def get(self):
        self.write_form()

    def post(self):
        self.write_form()
