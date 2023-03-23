import logging 

def get_logger():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        level=logging.DEBUG,
        filename='log.json')

    return logging.getLogger('scraping')