import time

from parser.parser import run_website_parser


LOADING_FROM_WEBSITE_PERIOD_MIN = 60
LOADING_FROM_WEBSITE_PERIOD_SEC = LOADING_FROM_WEBSITE_PERIOD_MIN * 60


if __name__ == '__main__':
    while True:
        run_website_parser()
        time.sleep(LOADING_FROM_WEBSITE_PERIOD_SEC)
