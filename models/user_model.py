import header as h


class User(h.db.Model):
    username = h.db.StringProperty(required=True)
    password = h.db.StringProperty(required=True)
    email = h.db.StringProperty(required=True)
    created = h.db.DateTimeProperty(auto_now_add=True)
    last_modified = h.db.DateTimeProperty(auto_now=True)
