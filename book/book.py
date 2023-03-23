import re
from utils.logger import get_logger

from locators.bookLocator import BookLocator


logger = get_logger('scraping.book')


class Book:
    def __init__(self, book: str) -> str:
        logger.debug('New book parser.')
        self.book = book

    def __repr__(self) -> str:
        return f'<Book "{self.title}" written by "{self.author}".>'

    @property
    def title(self) -> str:
        logger.debug(f'Finding book name using locator: `{BookLocator.TITLE}`.')
        title = self.book.select_one(BookLocator.TITLE).string.strip()
        logger.debug(f'Found book name: `{title}`.')
        return title

    @property
    def url(self) -> str:
        logger.debug(f'Finding book url using locator: `{BookLocator.URL}`.')
        url_tag = self.book.select_one(BookLocator.URL)
        url = str(url_tag.attrs.get('href')).strip()
        logger.debug(f'Found book url: `{url}`.')
        return url

    @property
    def author(self) -> str:
        logger.debug(f'Finding book author using locator: `{BookLocator.AUTHOR}`.')
        try:
            author = self.book.select_one(BookLocator.AUTHOR).text.strip()
        except:
            author = None
        logger.debug(f'Found book author: `{author}`.')
        return author

    @property
    def description(self) -> str:
        logger.debug(f'Finding book description using locator: `{BookLocator.DESCRIPTION}`.')
        description = self.book.select_one(
            BookLocator.DESCRIPTION).string.strip()
        logger.debug(f'Found book description: `{description[:15]}`.')
        return description

    @property
    def status(self) -> str:
        logger.debug(f'Finding book availabiblity status using locator: `{BookLocator.STATUS}`.')
        status = self.book.select_one(BookLocator.STATUS).text.strip()
        logger.debug(f'Found book availabiblity statu: `{status}`.')
        return status

    @property
    def price(self) -> float:
        logger.debug(f'Finding book price using locator: `{BookLocator.PRICE}`.')
        price_str = self.book.select_one(BookLocator.PRICE).string
        logger.debug(f'Found book price tag: `{price_str}`.')
        price_pattern = '([0-9]+,[0-9]+) €'
        price = float(re.search(price_pattern, price_str)[1].replace(',', '.'))
        logger.debug(f'Converted book (float) price: `{price}`.')
        return price

    @property
    def image(self) -> str:
        logger.debug(f'Finding book image using locator: `{BookLocator.IMAGE}`.')
        image_tag = self.book.select_one(BookLocator.IMAGE)
        image = str(image_tag.attrs.get('data-src')).strip()
        logger.debug(f'Found book image: `{image}`.')
        return image
