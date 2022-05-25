import scrapy


class AptarSpider(scrapy.Spider):
    name = 'aptar_spider'
    allowed_domains = ['www.aptar.com']
    start_urls = ['https://www.aptar.com/product-solutions/']
    
    def parse(self, response):
        pass
