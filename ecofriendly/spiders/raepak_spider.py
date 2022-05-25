import scrapy


class RaepakSpider(scrapy.Spider):
    name = 'raepak_spider'
    allowed_domains = ['www.raepak.com']
    start_urls = ['https://www.raepak.com/products/']
    
    def parse(self, response):
        for link in response.css('div.product div.col-inner a::attr(href)'):
            yield response.follow(link, callback=self.parse_category)
    
    def parse_category(self, response):
        for link in response.css('div.product div.col-inner a::attr(href)'):
            yield response.follow(link, callback=self.parse_subcategory)
    
    def parse_subcategory(self, response):
        for link in response.css('p.name a::attr(href)'):
            if '?' not in link.get():
                yield response.follow(link, callback=self.parse_category)
    
    def parse_product(self, response):
        yield {'name': response.css('h1.product-title::text').get().strip()}
