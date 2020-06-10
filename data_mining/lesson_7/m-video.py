from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

mongo_database = MongoClient('mongodb://localhost:27017')['m_video_db']
collection = mongo_database['bestsellers']


driver = webdriver.Chrome()

url = 'https://www.mvideo.ru'

driver.get(url)

try:
    bestsellers = driver.find_element_by_xpath(
        '//div[contains(text(),"Хиты продаж")]/ancestor::div[@data-init="gtm-push-products"]'
    )
except exceptions.NoSuchElementException:
    print('Bestsellers has not been found')

while True:
    try:
        next_button = WebDriverWait(bestsellers, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[class="next-btn sel-hits-button-next"]')
            )
        )

        driver.execute_script("$(arguments[0]).click();", next_button)
    except exceptions.TimeoutException:
        print('Сбор данных окончен')
        break

products = bestsellers.find_elements_by_css_selector('li.gallery-list-item')

for product in products:

    item = {}

    item['title'] = product.find_element_by_css_selector(
        'a.sel-product-tile-title').get_attribute('innerHTML')

    item['product_link'] = product.find_element_by_css_selector(
        'a.sel-product-tile-title').get_attribute('href')

    item['price'] = float(
        product.find_element_by_css_selector(
            'div.c-pdp-price__current').get_attribute('innerHTML').replace(
                '&nbsp;', '').replace('¤', ''))

    item['image_link'] = product.find_element_by_css_selector(
        'img[class="lazy product-tile-picture__image"]').get_attribute('src')

    collection.insert_one(item)
    collection.update_one({'product_link': item['product_link']}, {'$set': item}, upsert=True)

driver.quit()
