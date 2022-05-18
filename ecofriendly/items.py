import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def stringify(items):
    processed_items = []
    for item in items:
        processed_items.append(item.strip())
    
    return ', '.join(processed_items)


class EcofriendlyItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    description = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    details = scrapy.Field(input_processor=MapCompose(stringify), output_processor=TakeFirst)
    categories = scrapy.Field(input_processor=MapCompose(stringify), output_processor=TakeFirst)
    tags = scrapy.Field(input_processor=MapCompose(stringify), output_processor=TakeFirst)
