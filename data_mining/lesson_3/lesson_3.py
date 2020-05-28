from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
import requests
import re
from pprint import pprint


def parser_superjob(vacancy):

    vacancy_info = []

    params = {
        'keywords': vacancy,
        'page': ''
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    url = 'https://www.superjob.ru/vacancy/search/'

    response = requests.get(url, params=params, headers=headers)

    soup = bs(response.text, 'lxml')

    page_block = soup.find('a', {'class': 'f-test-button-1'})

    if not page_block:
        last_page = 1
    else:
        page_block = page_block.findParent()
        last_page = int(page_block.find_all('a')[-2].getText())

    for page in range(0, last_page + 1):
        params['page'] = page
        html = requests.get(url, params=params, headers=headers)

    soup = bs(html.text, 'lxml')

    vacancy_items = soup.find_all('div', {'class': 'f-test-vacancy-item'})

    for item in vacancy_items:
        vacancy_info.append(item_superjob(item))

    return vacancy_info

def item_superjob(item):

    vacancy_info = {}

    vacancy_name = item.find('a').getText()

    vacancy_info['vacancy_name'] = vacancy_name

    company_name = item.find('span', {'class': 'f-test-text-vacancy-item-company-name'})

    if not company_name:
        company_name = item.findParent().find('span', {'class': 'f-test-text-vacancy-item-company-name'}).getText()
    else:
        company_name = company_name.getText()

    vacancy_info['company_name'] = company_name

    vacancy_city = item.find('span', {'class': 'f-test-text-company-item-location'}).findChildren()[2].getText().split(',')

    vacancy_info['vacancy_city'] = vacancy_city[0]

    salary = item.find('span', {'class': 'f-test-text-company-item-salary'}).getText()

    if not salary or salary == 'По договорённости':
        salary_min = None
        salary_max = None
        salary_currency = None

    else:

        salary_split = salary.replace(u'\xa0', u' ').split(' ')
        salary_currency = salary_split[-1]

        if salary_split[0] == 'до':
            salary_min = None
            salary_max = int(salary_split[1] + salary_split[2])
        elif salary_split[0] == 'от':
            salary_min = int(salary_split[1] + salary_split[2])
            salary_max = None
        else:
            salary_min = int(salary_split[0] + salary_split[1])
            salary_max = int(salary_split[-3] + salary_split[-2])

    vacancy_info['salary_min'] = salary_min
    vacancy_info['salary_max'] = salary_max
    vacancy_info['salary_currency'] = salary_currency

    vacancy_url = item.find_all('a')

    if len(vacancy_url) > 1:
        vacancy_url = vacancy_url[-2]['href']
    else:
        vacancy_url = vacancy_url[0]['href']

    vacancy_info['vacancy_url'] = f'https://www.superjob.ru{vacancy_url}'

    vacancy_info['site'] = 'www.superjob.ru'

    return vacancy_info


def parser_hh(vacancy):
    url = 'https://hh.ru/search/vacancy'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    params = {
        'text': vacancy,
        'search_field': 'name',
        'items_on_page': '100',
        'page': ''
    }

    response = requests.get(url, params=params, headers=headers)
    soup = bs(response.text, 'lxml')

    vacancy_info = []

    page_block = soup.find('div', {'data-qa': 'pager-block'})

    if not page_block:
        last_page = '1'
    else:
        last_page = int(page_block.find_all('a', {'class': 'HH-Pager-Control'})[-2].getText())

    for page in range(0, last_page):
        params['page'] = page
        html = requests.get(url, params=params, headers=headers)

    soup = bs(html.text, 'lxml')

    vacancy_items = soup.find('div', {'data-qa': 'vacancy-serp__results'}).find_all('div',
                                                                                    {'class': 'vacancy-serp-item'})

    for item in vacancy_items:
        vacancy_info.append(item_hh(item))

    return vacancy_info

def item_hh(item):

    vacancy_info = {}

    vacancy_name = item.find('span', {'class': 'resume-search-item__name'}).getText().replace(u'\xa0', u' ')

    vacancy_info['vacancy_name'] = vacancy_name

    company_name = item.find('div', {'class': 'vacancy-serp-item__meta-info'}).find('a').getText()

    vacancy_info['company_name'] = company_name

    vacancy_city = item.find('span', {'class': 'vacancy-serp-item__meta-info'}).getText().split(', ')[0]

    vacancy_info['vacancy_city'] = vacancy_city

    salary = item.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
    if not salary:
        salary_min = None
        salary_max = None
        salary_currency = None
    else:
        salary = salary.getText().replace(u'\xa0', u'')

        salary = re.split(r'\s|-', salary)

        if salary[0] == 'до':
            salary_min = None
            salary_max = int(salary[1])
        elif salary[0] == 'от':
            salary_min = int(salary[1])
            salary_max = None
        else:
            salary_min = int(salary[0])
            salary_max = int(salary[-2])

        salary_currency = salary[-1]

    vacancy_info['salary_min'] = salary_min
    vacancy_info['salary_max'] = salary_max
    vacancy_info['salary_currency'] = salary_currency


    vacancy_url = item.find('span', {'class': 'resume-search-item__name'}).find('a')['href']

    vacancy_info['vacancy_url'] = vacancy_url[:vacancy_url.find('?')]

    vacancy_info['site'] = 'hh.ru'

    return vacancy_info


"""

1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB.
Реализовать функцию, записывающую собранные вакансии в созданную БД.

"""

def parser_vacancy_mongo(vacancy):

    vacancy_info = []
    vacancy_info.extend(parser_hh(vacancy))
    vacancy_info.extend(parser_superjob(vacancy))

    client = MongoClient('mongodb://localhost:27017')
    db = client['vacancy']
    collection = db['vacancy']
    collection.insert_many(vacancy_info)

    return collection

# vacancy = 'Python'
# parser_vacancy_mongo(vacancy)


'''

Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.

'''

def find_greater_then(number):

    client = MongoClient('mongodb://localhost:27017')
    db = client['vacancy']
    collection = db['vacancy']
    number_usd = number/71.39   # поскольку есть другие валюты в базе, а число мы вводим одно
    number_kzt = number/0.17
    number_eur = number/78.21
    number_gr = number/2.65
    result = collection.find(
        {'$or':[
            {'salary_currency': 'руб.',
             '$or': [
                 {'salary_min': {'$gte': number}},  # ищет в столбце и с минимальной, и с максимальной зарплатой
                 {'salary_max': {'$gte': number}}
             ]},
            {'salary_currency': 'USD',
             '$or': [
                 {'salary_min': {'$gte': number_usd}},
                 {'salary_max': {'$gte': number_usd}}
             ]},
            {'salary_currency': 'EUR',
             '$or': [
                 {'salary_min': {'$gte': number_eur}},
                 {'salary_max': {'$gte': number_eur}}
             ]},
            {'salary_currency': 'грн.',
             '$or': [
                 {'salary_min': {'$gte': number_gr}},
                 {'salary_max': {'$gte': number_gr}}
             ]},
            {'salary_currency': 'KZT',
             '$or': [
                 {'salary_min': {'$gte': number_kzt}},
                 {'salary_max': {'$gte': number_kzt}}
             ]}
        ]},
        {'_id': 0}
    )

    result.sort('salary_min', -1)

    return result

number = 50000

greater_then = find_greater_then(number)
for obj in greater_then:
    pprint(obj)

