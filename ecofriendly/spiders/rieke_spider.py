import scrapy


class RiekeSpiderSpider(scrapy.Spider):
    name = 'rieke_spider'
    allowed_domains = ['www.riekepackaging.com']
    start_urls = ['https://www.riekepackaging.com/products-by-range']
    
    def parse(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_parts)
    
    def parse_parts(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)
    
    def parse_categories(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_subcategories)
    
    def parse_subcategories(self, response):
        for link in response.css('a.category__name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_item)
    
    def parse_item(self, response):
        name = response.css('h1.product__title::text').get()
        data = response.css('div.grid-x.scene_element')
        specifications = {}
        for row in data:
            key = ' '.join(map(str.strip, row.css('h2::text').getall()))
            feats = row.css('div.li-container::text').getall()
            count = 1
            values = []
            for i in range(len(feats)):
                if feats[i] != '\n':
                    values.append(f'{count}. {feats[i].strip()}')
                    count += 1
            specifications[key] = '\n'.join(values)
        yield {'name': name, 'specifications': specifications}
