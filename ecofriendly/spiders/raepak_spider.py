from scrapy.loader import ItemLoader
from ecofriendly.items import RaepakItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RaepakSpider(CrawlSpider):
    name = 'raepak_spider'
    allowed_domains = ['www.raepak.com']
    start_urls = ['https://www.raepak.com/products/']
    
    rules = (
        Rule(LinkExtractor(restrict_css='div.product-category div.col-inner a'), follow=True),
        Rule(LinkExtractor(restrict_css='div.box-image div.image-zoom_in a'), callback='parse_items'),
    )
    
    def parse_items(self, response):
        item = ItemLoader(item=RaepakItem(), response=response)
        item.add_css('name', 'h1.product-title')
        item.add_css('category', 'div.product_meta span.posted_in')
        item.add_css('description', 'div.product-short-description p:nth-child(1)')
        item.add_css('dimension_sku', 'div.accordion-inner table')
        item.add_css('product_information', 'div.tab-panels table.woocommerce-product-attributes.shop_attributes')
        yield item.load_item()
