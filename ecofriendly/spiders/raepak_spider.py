import scrapy


class RaepakSpider(scrapy.Spider):
    name = 'raepak_spider'
    allowed_domains = ['www.raepak.com']
    start_urls = ['https://www.raepak.com/products/']
    
    def parse(self, response):
        pass
