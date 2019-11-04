from pymongo import MongoClient
from pymongo import ASCENDING


client = MongoClient('db', 27017)
db = client.databse
posts = db.posts
default_order = ('_id', ASCENDING)


def get_pikabu_posts(limit=None, offset=None, order=default_order):
    """
    Get pikabu posts

    Args:
        * limit (int): limit of posts' count
        * offset (int): offset of posts'
        * order (tuple): posts' order
    """
    result = posts.find({})
    return result
