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


class ROT13Handler(webapp2.RequestHandler):
    def rot13(self, s):
        new_str = ''
        for char in s:
            if char in string.ascii_letters:
                offset = (ord('a') if char.islower() else ord('A'))
                num = ord(char) - offset
                new_char = chr(num + 13 + offset)  if num + 13 < 26 else \
                    chr(((num + 12) - 25) + offset)
                new_str += new_char
            else:
                new_str += char
        return new_str

    def write_form(self, text=""):
        self.response.out.write(form.format(**{"text": text}))

    def get(self):
        self.write_form()

    def post(self):
        user_string = self.request.get('text')
        rot13_text = self.rot13(user_string)
        valid_text = escape_html(rot13_text)
        self.write_form(valid_text)
