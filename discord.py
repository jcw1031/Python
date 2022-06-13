from re import I
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/jcw/Coding/Python/chromedriver')
driver.get('https://discord.com/channels/983476601197068378/985123191762587679')
time.sleep(4)

e = driver.find_elements_by_class_name('marginTop8-24uXGp')[0]
e.send_keys(Keys.ENTER)

e = driver.find_elements_by_class_name('inputDefault-3FGxgL')[0]
e.send_keys('jcw001031@gmail.com')

e = driver.find_elements_by_class_name('inputDefault-3FGxgL')[1]
e.send_keys('Chan!1057')

e = driver.find_elements_by_class_name('marginBottom8-emkd0_')[1]
e.send_keys(Keys.ENTER)

time.sleep(7)

while True:
    e = driver.find_elements_by_class_name('DraftEditor-root')[0]
    e = driver.find_elements_by_class_name('fontSize16Padding-XoMpjI')[1]
    e.send_keys('!강화 성공')
    e.send_keys(Keys.ENTER)
    time.sleep(62)
