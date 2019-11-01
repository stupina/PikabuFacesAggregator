import urllib3
from bs4 import BeautifulSoup
from parser.settings import URL


def run_website_parser():
    print("LPLP")
    req = urllib3.PoolManager()
    print("1")
    print(URL.format('1'))
    res = req.request('GET', URL.format('1'))
    print("2")
    soup = BeautifulSoup(res.data, 'html.parser')
    print("3")
    articles = soup.findAll('article', class_='story')
    print("END")
