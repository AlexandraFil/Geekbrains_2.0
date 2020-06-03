# -*- coding: utf-8 -*-
import scrapy
from vacancy_parse.items import VacancyParseItem


class SuperjobParseSpider(scrapy.Spider):
    name = 'superjob_parse'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=Python']

    def parse(self, response):

        pagination = response.xpath('//div[contains(@class, "_GJem")]//a/@href')
        for link in pagination:
            yield response.follow(link, callback=self.parse)

        vacancies = response.xpath('//div[contains(@class, "f-test-vacancy-item")]//a[@target = "_blank"]/@href')
        for link in vacancies:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response):

        vacancy_name = response.xpath('//div//h1/text()').extract_first()
        salary = response.xpath('//span[contains(@class,"ZON4b PlM3e")]//text()').extract()

        if salary:

            if salary[0] == 'до':
                salary_min = None
                salary = salary[2].replace(u'\xa0', u' ').split()
                salary_max = int(salary[0]+salary[1])
                salary_currency = salary[-1]
            elif salary[0] == 'от':
                salary_max = None
                salary = salary[2].replace(u'\xa0', u' ').split()
                salary_min = int(salary[0] + salary[1])
                salary_currency = salary[-1]
            elif salary[0] == 'По договорённости':
                salary_min = None
                salary_max = None
                salary_currency = None
            else:
                salary_min = int(salary[0].replace(u'\xa0', u''))
                salary_max = int(salary[-3].replace(u'\xa0', u''))
                salary_currency = salary[-1]

        else:
                salary_min = None
                salary_max = None
                salary_currency = None

        vacancy_link = response.url
        vacancy_source = 'superjob.ru'

        item = VacancyParseItem(
            vacancy_name = vacancy_name,
            salary_min = salary_min,
            salary_max = salary_max,
            salary_currency = salary_currency,
            vacancy_link = vacancy_link,
            vacancy_source = vacancy_source
        )
        yield item
