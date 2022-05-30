import scrapy
from scrapy.loader import ItemLoader
from ecofriendly.items import VirospackItem


class VirospackSpider(scrapy.Spider):
    name = 'virospack_spider'
    allowed_domains = ['virospack.com']
    start_urls = ['https://virospack.com/products/catalogue/']
    
    def parse(self, response):
        for link in response.css('div.item a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_item)
    
    def parse_item(self, response):
        item = ItemLoader(item=VirospackItem(), response=response)
        description = '\n'.join(response.css('div.content-text.col-md-6 p::text').getall())
        table_data = response.css('div.product-description-outer')[0]
        keys = table_data.css('div.product-description-left::text').getall()
        values = table_data.css('div.product-description-right::text').getall()
        notice = keys[-1] if len(keys) > len(values) else None
        data = dict(zip(keys, values))
        item.add_css('name', 'div.content-title h2')
        item.add_css('code', 'div.product-description h6')
        item.add_value('data', data)
        item.add_value('description', description)
        item.add_value('notice', notice)
        yield item.load_item()
