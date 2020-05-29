from lxml import html
import requests
from datetime import datetime

def get_news_yandex():

    news = []

    keys = ('title', 'date', 'link')

    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36'
    }

    link = 'https://yandex.ru/news/'
    request = requests.get(link, headers=headers)

    root = html.fromstring(request.text)
    root.make_links_absolute('https://yandex.ru/news/')

    news_links = root.xpath('//div[@class = "story__topic"]//a[contains(@class, "link_theme_black")]/@href')

    news_titles = root.xpath('//div[@class = "story__topic"]//a[contains(@class, "link_theme_black")]/text()')

    news_dates = root.xpath('//div[@class = "story__date"]/text()')

    for i in range(len(news_dates)):
        date = str(datetime.date(datetime.now()))
        news_dates[i] = datetime.strptime(date + news_dates[i][-5:], '%Y-%m-%d%H:%M')

    for item in list(zip(news_titles, news_dates, news_links)):
        news_dict = {}
        for key, value in zip(keys, item):
            news_dict[key] = value

        news_dict['source'] = 'yandex.ru/news/'
        news.append(news_dict)

    return news