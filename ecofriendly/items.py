import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst, MapCompose


def stringify_list(items):
    processed_items = []
    for item in items:
        processed_items.append(item.strip())
    
    return ', '.join(processed_items)


class EcofriendlyItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    description = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    details = scrapy.Field(input_processor=MapCompose(stringify_list), output_processor=TakeFirst)
    categories = scrapy.Field(input_processor=MapCompose(stringify_list), output_processor=TakeFirst)
    tags = scrapy.Field(input_processor=MapCompose(stringify_list), output_processor=TakeFirst)


class FusionItem(scrapy.Item):
    product_name = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    details = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    uses = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)
    specifications = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst)


class RaepakItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
    category = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
    dimension_sku = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
    product_information = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
