from re import I
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/jcw/Coding/Python/chromedriver')
driver.get('https://instagram.com')

time.sleep(2)

e = driver.find_elements_by_class_name('_2hvTZ')[0]
e.send_keys('jcw001031@icloud.com')

e = driver.find_elements_by_class_name('_2hvTZ')[1]
e.send_keys('Chan!1057')
e.send_keys(Keys.ENTER)

time.sleep(3)

e = driver.find_elements_by_class_name('sqdOP')[0]
e.send_keys(Keys.ENTER)

time.sleep(3)

e = driver.find_element_by_class_name('HoLwm')
e.send_keys(Keys.ENTER)

e = driver.find_element_by_class_name('gmFkV')
e.send_keys(Keys.ENTER)

e = driver.find_element_by_class_name('_9AhH0')
e.send_keys(Keys.ENTER)