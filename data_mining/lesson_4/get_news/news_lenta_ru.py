from lxml import html
import requests
from datetime import datetime

def get_news_lenta():

    news = []

    keys = ('title', 'date', 'link')
    date_format = '%Y-%m-%dT%H:%M:%S%z'

    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36'
     }

    link = 'https://lenta.ru/'
    request = requests.get(link, headers=headers)

    root = html.fromstring(request.text)
    root.make_links_absolute('https://lenta.ru/')

    news_links = root.xpath('''(//section[@class="row b-top7-for-main js-top-seven"]//div[@class="first-item"]/h2 |
                                //section[@class="row b-top7-for-main js-top-seven"]//div[@class="item"])
                                /a/@href''')

    news_titles = root.xpath('''(//section[@class="row b-top7-for-main js-top-seven"]//div[@class="first-item"]/h2 |
                                //section[@class="row b-top7-for-main js-top-seven"]//div[@class="item"])
                                /a/text()''')

    for i in range(len(news_titles)):
        news_titles[i] = news_titles[i].replace(u'\xa0', u' ')

    news_dates = []

    for item in news_links:
        request = requests.get(item, headers=headers)
        root = html.fromstring(request.text)
        date = root.xpath('//time[@class="g-date"]/@datetime')
        news_dates.extend(date)

    for i in range(len(news_dates)):
        news_dates[i] = datetime.strptime(news_dates[i], date_format)

    for item in list(zip(news_titles, news_dates, news_links)):
        news_dict = {}
        for key, value in zip(keys, item):
            news_dict[key] = value

        news_dict['source'] = 'lenta.ru'
        news.append(news_dict)

    return news