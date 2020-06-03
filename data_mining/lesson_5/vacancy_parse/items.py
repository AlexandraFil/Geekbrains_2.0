# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VacancyParseItem(scrapy.Item):
    _id = scrapy.Field()
    vacancy_name = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    salary_currency = scrapy.Field()
    vacancy_link = scrapy.Field()
    vacancy_source = scrapy.Field()