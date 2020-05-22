from bs4 import BeautifulSoup as bs
import requests


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


