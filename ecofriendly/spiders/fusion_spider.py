import scrapy


class FusionSpider(scrapy.Spider):
    name = 'fusion_spider'
    allowed_domains = ['fusionpkg.com']
    start_urls = ['https://fusionpkg.com/shop/']
    
    def parse(self, response):
        for link in response.css('a.learn-more-button::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_item)
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_item(self, response):
        pass
