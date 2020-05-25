from bs4 import BeautifulSoup as bs
import requests
import re


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


def parser_hh(vacancy):
    vacancy = 'Python'

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

    vacancy_items = soup.find('div', {'data-qa': 'vacancy-serp__results'}).find_all('div', {'class': 'vacancy-serp-item'})

    for item in vacancy_items:
        vacancy_info.append(item_hh(item))

