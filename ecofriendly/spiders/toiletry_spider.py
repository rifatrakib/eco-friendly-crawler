import scrapy
from ecofriendly.items import EcofriendlyItem


class ToiletrySpider(scrapy.Spider):
    name = 'toiletry_spider'
    allowed_domains = ['www.sgcclosures.com']
    start_urls = ['https://www.sgcclosures.com/product-category/']
    
    def parse(self, response):
        for link in response.css('li.product-category a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)
    
    def parse_categories(self, response):
        for link in response.css('div.product-wrap a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_products)
    
    def parse_products(self, response):
        item = EcofriendlyItem()
        item['name'] = response.css('h1.product_title::text').get()
        item['description'] = response.css('div.woocommerce-product-details__short-description p::text').get()
        item['details'] = response.css('div.woocommerce-product-details__short-description ul li::text').getall()
        item['categories'] = response.css('span.posted_in a::text').getall()
        item['tags'] = response.css('span.tagged_as a::text').getall()
        yield item
