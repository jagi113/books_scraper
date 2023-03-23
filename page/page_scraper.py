from bs4 import BeautifulSoup
from utils.logger import get_logger

from book.book import Book
from locators.pageLocator import PageLocator


logger = get_logger('scraping.page_scraper')


class PageScraper:
    def __init__(self, page: str) -> BeautifulSoup:
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.page = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = PageLocator.BOOKS
        logger.debug(f'Finding all books in the page using locator: `{locator}`.')
        books = [book
                 for book
                 in self.page.select(locator)
                 if 'listing-promo' not in book.attrs.get('class')
                 ]
        return [Book(book) for book in books]
    
    def page_count(self):
        logger.debug(f'Finding all number of catalogue pages available...')
        locator = PageLocator.PAGE_COUNT
        page_count = int(self.page.select_one(locator).text.strip())
        logger.debug(f'Found number of catalogue pages available: `{page_count}`')
        return page_count
