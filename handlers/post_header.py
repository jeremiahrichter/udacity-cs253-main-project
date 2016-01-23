from google.appengine.api import memcache
from models.post_model import Post
import time
import header as h
from header import blog_key


def top_ten(update=False):
    key = 'top10'
    posts = memcache.get(key)
    if posts is None or update:
        posts = (list(Post.all().order('-created').run(limit=10)), time.time())
        memcache.set(key, posts)
    return posts


def get_post(post_id):
    post = memcache.get(post_id)
    if not post:
        key = h.db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = h.db.get(key), time.time()
        post and memcache.set(post_id, post)
    return post
