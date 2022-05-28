import scrapy


class RiekeSpiderSpider(scrapy.Spider):
    name = 'rieke_spider'
    allowed_domains = ['www.riekepackaging.com']
    start_urls = ['https://www.riekepackaging.com/products-by-range']
    
    def parse(self, response):
        for link in response.css('a.filters__link::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)
    
    def parse_categories(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_subcategories)
    
    def parse_subcategories(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_items)
    
    def parse_items(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_item)
    
    def parse_item(self, response):
        yield {'name': response.css('h1.product__title::text').get()}
