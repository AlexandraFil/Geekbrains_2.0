# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from leroymerlin.items import LeroymerlinItem

class LeroymerlinParseSpider(scrapy.Spider):
    name = 'leroymerlin_parse'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/catalogue/podvesnye-svetilniki/']


    xpt_str = {
        'name' : '//h1/text()',
        'photos' : '//picture[@slot="pictures"]//img/@src',
        'price' : '//span[@slot="price"]/text()',
    }


    def __init__(self):
        super().__init__()

    def parse(self, response):

        pagination = response.xpath('//div[contains(@class, "list-paginator")]//a[contains(@class, "paginator-item")]/@href')
        for link in pagination:
            yield response.follow(link, callback=self.parse)

        items = response.xpath('//div[contains(@class, "product-name")]/a[contains(@class, "product-name-inner")]/@href')
        for link in items:
            yield response.follow(link, callback=self.items_parse)

    def items_parse(self, response):

        item = ItemLoader(LeroymerlinItem(), response)

        for key, value in self.xpt_str.items():
            item.add_xpath(key, value)

        definition_term = response.xpath(
            '//dl[contains(@class, "def-list")]//dt[@class="def-list__term"]/text()').extract()
        definition_def = response.xpath(
            '//dl[contains(@class, "def-list")]//dd[@class="def-list__definition"]/text()').extract()
        for i in range(len(definition_def)):
            definition_def[i] = ' '.join(definition_def[i].split())

        definition = dict(zip(definition_term, definition_def))
        float_list = ['(мм)', '(кг)', '(в м²)', '(см)', '(лет)']
        int_list = ['(в K)', '(Вт)', '(В)']
        for key in definition.keys():
            if key in float_list:
                definition[key] = float(definition[key])
            if key in int_list:
                definition[key] = int(definition[key])

        item.add_value('definition', definition)

        yield item.load_item()
