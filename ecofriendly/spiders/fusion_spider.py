import scrapy
from ecofriendly.items import FusionItem


class FusionSpider(scrapy.Spider):
    name = 'fusion_spider'
    allowed_domains = ['fusionpkg.com']
    start_urls = ['https://fusionpkg.com/shop/']
    
    def extract_specifications_data(self, specs):
        data = {}
        for spec in specs:
            items = spec.css('li')
            for item in items:
                key = item.css('span.spec-label::text').get()
                if key:
                    if item.css('ul'):
                        values = []
                        for value in item.css('ul li::text'):
                            values.append(str(value).split('[] =>')[1].strip("\\n)\\n'>").strip())
                        data[key] = ', '.join(values)
                    elif item.css('span.te'):
                        data[key] = ', '.join(item.css('span.te::text').getall())
                    else:
                        data[key] = item.css('span:nth-child(2)::text').get()
        
        return data
    
    def stringify_dict(self, data):
        processed_items = []
        count = 1
        for key, value in data.items():
            if key.endswith('#'):
                key = key.replace('#', 'number')
            key = key.lower().replace(' ', '_')
            item_data = f'{count}. {key}: {value}'
            processed_items.append(item_data)
            count += 1
        
        return '\n'.join(processed_items)
    
    def parse(self, response):
        for link in response.css('a.learn-more-button::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_item)
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_item(self, response):
        product_name = response.css('h1.product_title::text').get()
        details = response.css('div.et_pb_module_inner p::text').get()
        uses = response.css('div.et_pb_text_3 div.et_pb_text_inner::text').get()
        
        specs = response.css('div.specificaion-inner-right ul li')
        data = self.extract_specifications_data(specs)
        processed_data = self.stringify_dict(data)
        
        item = FusionItem()
        item['product_name'] = product_name
        item['details'] = details
        item['uses'] = uses
        item['specifications'] = processed_data
        yield item
