import hashlib
import hmac
import random
import string

ALPHA_NUM = string.letters + string.digits


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    return "{0},{1}".format(hashlib.sha256(name + pw + salt).hexdigest(), salt)


def make_salt():
    return "".join([str(random.choice(ALPHA_NUM)) for x in range(0, 5)])


def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)


SECRET = 'ImASecret'


def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split("|")[0]
    return val if (h == make_secure_val(val)) else None
