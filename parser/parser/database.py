import datetime

from pymongo import MongoClient


client = MongoClient('db', 27017)
db = client.databse
posts = db.posts


def find_pikabu_post(external_id):
    """
    Find pikabu post by `external_id`

    Args:
        * external_id (str): Pikabu post's id from website

    Returns:
        * post (record): founded post
    """
    values = {
        'external_id': external_id,
    }
    post = db.posts.find_one(values)
    return post


def create_pikabu_post(title, images_urls, author, external_id, post_url):
    """
    Create pikabu post

    Args:
        * title (str): Pikabu post's title
        * images_urls(str): Images' urls from pikabu post with faces
        * author (str): Pikabu post's author
        * external_id (str): Pikabu post's id from website
        * post_url (str): Pikabu post's url

    Returns:
        * post_id (str): Id of create post
    """
    post = {
        'title': title,
        'images_urls': images_urls,
        'author': author,
        'external_id': external_id,
        'post_url': post_url,
        'date': datetime.datetime.utcnow(),
    }
    post_id = posts.insert_one(post).inserted_id
    return post_id
