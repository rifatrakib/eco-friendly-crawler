from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RaepakSpider(CrawlSpider):
    name = 'raepak_spider'
    allowed_domains = ['www.raepak.com']
    start_urls = ['https://www.raepak.com/products/']
    
    rules = (
        Rule(LinkExtractor(restrict_css='div.product-category div.col-inner a'), follow=True),
        Rule(LinkExtractor(restrict_css='p.name.product-title a'), callback='parse_items'),
    )
    
    def parse_items(self, response):
        yield {
            'name': response.css('h1.product-title'),
            'category': response.css('div.product_meta span.posted_in'),
            'description': response.css('div.product-short-description p:nth-child(1)'),
            'dimension_sku': response.css('div.accordion-inner table'),
            'product_information': response.css('div.tab-panels table.woocommerce-product-attributes.shop_attributes'),
        }
