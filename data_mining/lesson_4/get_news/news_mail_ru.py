from lxml import html
import requests
from datetime import datetime

def get_news_mail():

    news = []

    keys = ('title', 'date', 'link')
    date_format = '%Y-%m-%dT%H:%M:%S%z'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 Safari/537.36'
    }

    link = 'https://news.mail.ru/'
    request = requests.get(link, headers=headers)

    root = html.fromstring(request.text)
    root.make_links_absolute(link)

    news_links = root.xpath('(//div[contains(@class, "newsitem")] | '
                            '//span[@class = "list__text"])'
                            '//a/@href')

    news_titles = root.xpath('(//div[contains(@class, "newsitem")] | '
                             '//span[@class = "list__text"])'
                             '//a/span/text()')

    for i in range(len(news_titles)):
        news_titles[i] = news_titles[i].replace(u'\xa0', u' ')

    news_dates = []

    for item in news_links:
        request = requests.get(item, headers=headers)
        root = html.fromstring(request.text)
        date = root.xpath('//span[contains(@class, "note__text breadcrumbs__text")]/@datetime')
        news_dates.extend(date)

    for i in range(len(news_dates)):
        news_dates[i] = datetime.strptime(news_dates[i], date_format)

    for item in list(zip(news_titles, news_dates, news_links)):
        news_dict = {}
        for key, value in zip(keys, item):
            news_dict[key] = value

        news_dict['source'] = 'news.mail.ru'
        news.append(news_dict)

    return news
