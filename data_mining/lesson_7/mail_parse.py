from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options

def parse_email(element):

    item = {}

    item['from_name'] = driver.find_element_by_xpath('//span[@class="letter-contact"]').text
    item['from_email'] = driver.find_element_by_xpath('//span[@class="letter-contact"]').get_attribute('title')
    item['date'] = driver.find_element_by_xpath('//div[@class="letter__date"]').text
    item['title'] = driver.find_element_by_xpath('//h2[@class="thread__subject"]').text
    item['message_text'] = driver.find_element_by_xpath('//div[@class="letter-body__body"]').text.replace(u'\n', u'').replace(u'\u200c', u'')

    return item


driver = webdriver.Chrome()

mongo_database = MongoClient('mongodb://localhost:27017')['mail_db']
collection = mongo_database['messages']

url = 'https://mail.ru/'

driver.get(url)
login_field = driver.find_element_by_xpath("//input[@id = 'mailbox:login']")
login_field.send_keys('alexandra_panfilova')
domain_field = driver.find_element_by_xpath("//select[@id = 'mailbox:domain']")
domain_field.send_keys('@inbox.ru')
password_button = driver.find_element_by_xpath("//input[@value = 'Ввести пароль']")
password_button.click()
password_field = driver.find_element_by_xpath("//input[@id = 'mailbox:password']")
password_field.send_keys('32263226A')
password_field.send_keys(Keys.ENTER)
first_letter = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH , '//div[@class="dataset__items"]/a')))
first_letter.click()

while True:
    try:
        collection.insert_one(parse_email(driver))
        next_button = driver.find_element_by_xpath("//span[@title = 'Следующее']")
        if next_button.get_attribute('disabled'):
            print('E-mails are over')
            break
        else:
            next_button.click()
            # ActionChains(driver).key_down(Keys.CONTROL).send_keys('k').key_up(Keys.CONTROL).perform()
    except Exception:
        print('E-mails are over')
        break

driver.quit()


