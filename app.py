import requests
import logging 

from page.page_scraper import PageScraper

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='log.json')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

#page_count:int = PageScraper(requests.get('https://www.pantarhei.sk/knihy?p=1').content).page_count()

books=[]
for page in range(1):
    url = f'https://www.pantarhei.sk/knihy?p={page+1}'
    
    page_content = requests.get(url).content
    logger.info(f'Creating books from page: << {page+1} >>')
    books.extend(PageScraper(page_content).books)
    

if __name__ == "__main__":
    for book in books:
        print(book)