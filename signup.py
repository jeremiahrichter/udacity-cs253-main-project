import webapp2

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
<div class="error"></div>
</body>
</html>
"""


class SignupHandler(webapp2.RequestHandler):
    def write_form(self, username="", email="", error=""):
        self.response.out.write(form.format(**{'username': username,
                                               'email': email,
                                               'error': error}))


    def get(self):
        self.write_form()

    def post(self):
        self.write_form()
