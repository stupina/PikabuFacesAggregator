import urllib3
from bs4 import BeautifulSoup
from parser.settings import MAX_COUNT_OF_PARSED_PAGES, URL


def run_website_parser():
    req = urllib3.PoolManager()
    for page_number in range(1, MAX_COUNT_OF_PARSED_PAGES + 1):
        res = req.request('GET', URL.format('page_number'))
        soup = BeautifulSoup(res.data, 'html.parser')
        articles = soup.findAll('article', class_='story')
        for article in articles:
            external_id = article['data-story-id']
