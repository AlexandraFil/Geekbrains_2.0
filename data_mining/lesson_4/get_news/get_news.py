'''
Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex-новости.
Для парсинга использовать XPath. Структура данных должна содержать:
название источника;
наименование новости;
ссылку на новость;
дата публикации.
'''

import random

from news_mail_ru import get_news_mail
from news_lenta_ru import get_news_lenta
from news_yandex_ru import get_news_yandex

news = []
news.extend(get_news_mail())
news.extend(get_news_lenta())
news.extend(get_news_yandex())

print(random.choice(news))
