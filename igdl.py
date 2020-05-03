from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

user = 'theweeknd'

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('/mnt/c/Users/brian/chromedriver_win32/chromedriver.exe')
driver.get('https://imgtagram.com/u/' + user)
last_height = 0
for i in range(1,100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')