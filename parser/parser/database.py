import datetime

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.test_database
posts = db.posts


def create_pikabu_post(title, images_paths, author,
                       external_id, external_create_date):
    """
    Create pikabu post

    Args:
        title (str): Pikabu post's title
        images_paths (str): Images from pikabu post with faces paths
        author (str): Pikabu post's author
        external_id: Pikabu post's id from website
        external_create_date: Pikabu post's create date from website

    Returns:
        post_id (str): Id of create post
    """
    post = {
        'title': title,
        'images_paths': images_paths,
        'author': author,
        'external_id': external_id,
        'external_create_date': external_create_date,
        'date': datetime.datetime.utcnow(),
    }
    post_id = posts.insert_one(post).inserted_id.str
    return post_id
