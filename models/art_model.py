import header as h

class Art(h.db.Model):
    title = h.db.StringProperty(required=True)
    art = h.db.TextProperty(required=True)
    created = h.db.DateTimeProperty(auto_now_add=True)
    coords = h.db.GeoPtProperty()
