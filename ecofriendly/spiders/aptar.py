import json
import scrapy


class AptarSpider(scrapy.Spider):
    name = 'aptar_spider'
    allowed_domains = ['www.aptar.com']
    start_urls = ['https://www.aptar.com/product-solutions/']
    
    def start_requests(self):
        total_pages=19
        for page_number in range(total_pages):
            form_data = {
                'requests':[
                    {
                        'indexName': 'prod_products',
                        'params': f'hitsPerPage=15&analyticsTags=%5B%22%2Fproduct-solutions%2F%22%5D&query=&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page={page_number}&maxValuesPerFacet=200&facets=%5B%22features_technologies%22%2C%22regions%22%2C%22airless_size%22%2C%22airless_dosage%22%2C%22neck_finish%22%2C%22lotion_closure_size%22%2C%22lotion_dosage%22%2C%22lock_mechanism%22%2C%22metal_free%22%2C%22market.lvl0%22%2C%22product_solution.lvl0%22%5D&tagFilters=&analytics=false&clickAnalytics=true'
                    }
                ]
            }
            url = 'https://ktqfx9x58t-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.13.0); Browser (lite)&x-algolia-api-key=9351c3bba4959cda5fe97f1af1095783&x-algolia-application-id=KTQFX9X58T'
            request_body = json.dumps(form_data)
            yield scrapy.Request(url, method='POST', body=request_body, headers={'Content-Type': 'application/json; charset=UTF-8'})
    
    def parse(self, response):
        yield response.json()
