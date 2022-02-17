from re import I
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/jcw/Coding/Python/chromedriver')
driver.get('https://instagram.com')

time.sleep(4)

e = driver.find_elements_by_class_name('_2hvTZ')[0]
e.send_keys('jcw001031@gmail.com')

e = driver.find_elements_by_class_name('_2hvTZ')[1]
e.send_keys('Chan!10571057 ')
e.send_keys(Keys.ENTER)

