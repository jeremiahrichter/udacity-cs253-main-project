import re

import webapp2

from header import escape_html

form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign Up</title>
    <style type="text/css">
        .error {{
        color: red;
        }}
        .right {{
            text-align: right;
        }}
    </style>
</head>
<body>
<h1>Enter your details to sign up</h1>
<form method="post">
    <table>
        <tr>
            <td class="right">Username</td>
            <td><input type="text" name="username" value="{username}"></td>
        </tr>
        <tr>
            <td class="right">Password</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td class="right">Verify Password</td>
            <td><input type="password" name="verify"></td>
        </tr>
        <tr>
            <td class="right">Email</td>
            <td><input type="email" name="email" value="{email}"></td>
        </tr>
    </table>
    <br>
    <br>
    <input type="submit">
</form>
<div class="error">{error}</div>
</body>
</html>
"""

USER_REGEX = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_REGEX = re.compile(r"^[^\s<>/\'\"]{8,}$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


class SignupHandler(webapp2.RequestHandler):
    def valid_username(self, s):
        return USER_REGEX.match(s)

    def valid_password(self, s):
        return PASS_REGEX.match(s)

    def valid_email(self, s):
        return EMAIL_REGEX.match(s)

    def write_form(self, username="", email="", error=""):
        self.response.out.write(form.format(**{'username': username,
                                               'email': email,
                                               'error': error}))

    def get(self):
        self.write_form()

    def post(self):
        error_msg = ''
        user_name = self.request.get('username')
        user_pass = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        valid_user, valid_pass, valid_email = (self.valid_username(user_name),
                                               self.valid_password(user_pass),
                                               self.valid_email(user_email))
        if not valid_user:
            error_msg += 'Please enter a 3-20 character username of alphanumeric characters, dashes or underscores.<br>'
        if valid_pass and not (user_pass == user_verify):
            error_msg += 'Both passwords do not match.<br>'
        if not valid_pass:
            error_msg += 'Please enter a password at least 8 characters long without using <, >, \', / or ".<br>'
        if not valid_email:
            error_msg += 'Please enter a valid email address.<br>'

        if len(error_msg) > 0:
            self.write_form(escape_html(user_name),
                            escape_html(user_email),
                            error_msg)
        else:
            self.redirect('/signed-up-success')


class SignupSuccessHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("<h1>Thank you for signing up!</h1>")
