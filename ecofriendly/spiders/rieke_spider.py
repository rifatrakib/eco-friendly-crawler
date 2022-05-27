import scrapy


class RiekeSpiderSpider(scrapy.Spider):
    name = 'rieke_spider'
    allowed_domains = ['www.riekepackaging.com']
    start_urls = ['https://www.riekepackaging.com/products-by-range']
    
    def parse(self, response):
        pass
