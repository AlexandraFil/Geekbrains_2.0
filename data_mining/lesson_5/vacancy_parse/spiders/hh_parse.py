# -*- coding: utf-8 -*-
import scrapy
from vacancy_parse.items import VacancyParseItem


class HhParseSpider(scrapy.Spider):
    name = 'hh_parse'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?&text=Python']

    def parse(self, response):

        pagination = response.xpath('//a[contains(@class, "HH-Pager-Control")]/@href')
        for link in pagination:
            yield response.follow(link, callback=self.parse)

        vacancies = response.xpath('//span[contains(@class, "resume-search-item__name")]//a/@href')
        for link in vacancies:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response):

        vacancy_name = response.xpath('//div[contains(@class, "vacancy-title")]/h1/text()').extract_first()
        salary = response.xpath('//p[contains(@class, "vacancy-salary")]//text()').extract_first()

        try:
            salary = salary.replace(u'\xa0', u'').split()

            if salary[0] == 'до':
                salary_min = None
                salary_max = int(salary[1])
                salary_currency = salary[2]
            elif salary[0] == 'от':
                if salary[2] == 'до':
                    salary_min = int(salary[1])
                    salary_max = int(salary[3])
                    salary_currency = salary[4]
                else:
                    salary_min = int(salary[1])
                    salary_max = None
                    salary_currency = salary[2]
            else:
                salary_min = None
                salary_max = None
                salary_currency = None

        except Exception:
                salary_min = None
                salary_max = None
                salary_currency = None

        vacancy_link = response.url
        vacancy_source = 'hh.ru'

        item = VacancyParseItem(
            vacancy_name = vacancy_name,
            salary_min = salary_min,
            salary_max = salary_max,
            salary_currency = salary_currency,
            vacancy_link = vacancy_link,
            vacancy_source = vacancy_source
        )
        yield item
