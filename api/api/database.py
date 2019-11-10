import os

from pymongo import MongoClient


DB_NAME = os.environ['DB_NAME']
DB_PORT = int(os.environ['DB_PORT'])
client = MongoClient(DB_NAME, DB_PORT)
db = client.databse
posts = db.posts


def get_pikabu_posts(limit, offset):
    """
    Get pikabu posts

    Args:
        * limit (int): limit of posts' count
        * offset (int): offset of posts'
    """
    result = tuple(posts.find(
        limit=limit,
        skip=offset,
    ))
    return result
