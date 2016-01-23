from google.appengine.api import memcache
from models.post_model import Post
import time


def top_ten(update=False):
    key = 'top10'
    posts = memcache.get(key)
    if posts is None or update:
        posts = (list(Post.all().order('-created').run(limit=10)), time.time())
        memcache.set(key, posts)
    return posts
