from scrapy.exporters import CsvItemExporter
from scrapy import signals


class CSVPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    
    def spider_opened(self, spider):
        formatted_spider_name = spider.name.replace('_', '-').replace('-spider', '')
        self.file = open(f'data/{formatted_spider_name}-data.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
