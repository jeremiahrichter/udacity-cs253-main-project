import hashlib


def hash_str(s):
    return hashlib.md5(s).hexdigest()


def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))


def check_secure_val(h):
    s, hsh = h.split(",")
    return s if (hash_str(s) == hsh) else None
