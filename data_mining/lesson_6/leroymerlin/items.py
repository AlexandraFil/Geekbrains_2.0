# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def text_to_float(item):
    item = item[0].split()
    return float(''.join(item))

class LeroymerlinItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    price = scrapy.Field(input_processor=text_to_float, output_processor=TakeFirst())
    definition = scrapy.Field(output_processor=TakeFirst())
