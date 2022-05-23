import scrapy


class FusionSpider(scrapy.Spider):
    name = 'fusion_spider'
    allowed_domains = ['fusionpkg.com']
    start_urls = ['https://fusionpkg.com/shop/']
    
    def parse(self, response):
        pass
