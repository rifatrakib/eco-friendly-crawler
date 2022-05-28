import json
import scrapy
import pandas as pd
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst, MapCompose


def stringify_list(items):
    processed_items = []
    for item in items:
        processed_items.append(item.strip())
    
    return ', '.join(processed_items)


def table_to_dict(data):
    df = pd.read_html(data)[0].astype('str')
    for col in df.columns:
        df[col] = df[col].str.strip()
    return json.dumps(df.to_dict(orient='records'))


def column_to_dict(data):
    df = pd.read_html(data)[0].astype('str')
    info = {}
    for row in range(df.shape[0]):
        info[df.iloc[row, 0]] = df.iloc[row, 1]
    return json.dumps(info)


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
    dimension_sku = scrapy.Field(input_processor=MapCompose(table_to_dict), output_processor=TakeFirst())
    product_information = scrapy.Field(input_processor=MapCompose(column_to_dict), output_processor=TakeFirst())


class AptarItem(scrapy.Item):
    product_id = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    name = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    market = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    product_solution = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    neck_finish = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    regions = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    features_technologies = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())


class RiekeItem(scrapy.Item):
    name = scrapy.Field()
    specifications = scrapy.Field()
