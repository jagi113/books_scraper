import asyncio
import aiohttp
import async_timeout
import time
import requests

from utils.logger import logger
from page.page_scraper import PageScraper

async def fetch_page(session, url, page):      # This is coroutine function (it must be wraped to await)
    async with async_timeout.timeout(120):
        async with session.get(url) as response:        # fetches the url
            logger.info(f'Creating books from page: << {page} >>')
            return await response.text()        # we must also await response

async def get_multiple_pages(loop, *urls):      # Main function
    async with aiohttp.ClientSession(loop=loop) as session:     # creates a session in which loop will be executed
        tasks = [fetch_page(session, url, page) for url, page in urls]      
        grouped_tasks = asyncio.gather(*tasks)      # gathers all fetch requests and calls them
        return await grouped_tasks

    #startpage = 0
    #end_page = 5
    #end_page:int = PageScraper(requests.get('https://www.pantarhei.sk/knihy?p=1').content).page_count()
    
    
def get_books(start_page:int, end_page:int):
    
    logger.info(f'Loading books from pages "{start_page} - {end_page}')

    urls = [(f"https://www.pantarhei.sk/knihy?p={page}", page) 
            for page 
            in range(start_page, end_page)]   

    loop = asyncio.get_event_loop()
    start_time = time.time()
    pages:list[str] = loop.run_until_complete(get_multiple_pages(loop, *urls))
    loading_time = time.time()
    logger.info(f"Pages loaded in {loading_time - start_time}")
    
    logger.debug("Creating books from loaded pages.")
    books=[]
    for page in pages:
        page_books = PageScraper(page)
        books.extend(page_books.books)
        
    logger.info(f"Books read in {time.time() - loading_time}")
    return books


    
if __name__ == "__main__":
    books = get_books()
    for book in books:
        print(book)