from contextlib import contextmanager
from tempfile import NamedTemporaryFile

import cv2
import requests
import urllib3
from bs4 import BeautifulSoup

from parser.database import find_pikabu_post, create_pikabu_post
from parser.settings import MAX_COUNT_OF_PARSED_PAGES, URL


def run_website_parser():
    """
    Run pikabu website parsing page by page

    Functions:
        * create_posts_from_post_with_faces_on_images

    Extra Info:
        * if you want change website url or max count of pages,
          see parser.settings
        * articles' count on page is 15
    """
    req = urllib3.PoolManager()
    for page_number in range(1, MAX_COUNT_OF_PARSED_PAGES + 1):
        res = req.request('GET', URL.format(page_number))
        soup = BeautifulSoup(res.data, 'lxml')
        articles = soup.findAll('article', class_='story')
        create_posts_from_post_with_faces_on_images(articles)


def create_posts_from_post_with_faces_on_images(articles):
    """
    Create post if article doesn't exist in databse
    and there is faces on article's images

    Args:
        * articles (list): list of pikabu article html-components

    Functions:
        * find_pikabu_post
        * get_images_urls_with_faces
        * create_pikabu_post
    """
    for article in articles:
        external_id = article['data-story-id']
        if find_pikabu_post(external_id):
            continue
        images = article.findAll('img', class_='story-image__image')
        images_urls = [image['data-large-image'] for image in images]
        images_with_faces_urls = get_images_urls_with_faces(images_urls)
        if images_with_faces_urls:
            images_urls_str = ';'.join(images_urls)
            title_link = article.find('a', class_='story__title-link')
            post_url = title_link['href']
            title = title_link.get_text()
            author = article.find('a', class_='user__nick').get_text()
            create_pikabu_post(
                title=title,
                images_urls=images_urls_str,
                author=author,
                external_id=external_id,
                post_url=post_url,
            )


def get_images_urls_with_faces(images_urls):
    """
    Remove from list of images' urls urls without faces

    Args:
        * images_urls (list): list with images's urls

    Functions:
        * as_file
        * found_faces
    """
    for image_url in images_urls:
        with as_file(image_url) as filename:
            faces = found_faces(filename)
            if not len(faces):
                images_urls.remove(image_url)


@contextmanager
def as_file(url):
    """
    Open image url as file

    Args:
        * url (str): image's url
    """
    with NamedTemporaryFile() as tfile:
        tfile.write(requests.get(url).content)
        tfile.flush()
        yield tfile.name


def found_faces(image_path):
    """
    Found faces on image

    Args:
        * image_path (str): temporary image's path

    Returns:
        * faces (list): coordinates of faces on image
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades
        + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30),
    )
    return faces
