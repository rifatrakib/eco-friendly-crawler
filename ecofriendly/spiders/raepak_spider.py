import scrapy
import pandas as pd
from ecofriendly.items import RaepakItem

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
                yield response.follow(link, callback=self.parse_product)
    
    def parse_product(self, response):
        name = response.css('h1.product-title::text').get().strip()
        details = response.css('div.product-short-description p:nth-child(1)').get()
        category = response.css('span.posted_in a::text').get()
        product_information = self.stringify_dict(pd.read_html(response.css('div.accordion-inner table').get())[0].to_dict(orient='records'))
        additional_information = self.stringify_dict({row[0]: row[1] for row in pd.read_html(response.css('div.tab-panels table').get())[0].to_numpy()})
        
        item = RaepakItem()
        item['name'] = name
        item['details'] = details
        item['category'] = category
        item['product_information'] = product_information
        item['additional_information'] = additional_information
        yield item
    
    def stringify_dict(self, data):
        processed_items = []
        count = 1
        for key, value in data.items():
            key = key.lower().replace(' ', '_')
            item_data = f'{count}. {key}: {value}'
            processed_items.append(item_data)
            count += 1
        
        return '\n'.join(processed_items)
