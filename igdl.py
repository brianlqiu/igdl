from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import re
import pprint

def is_photo_link(tag):
    return tag.name == 'a' and tag.has_attr('href') and tag['href'].find('/m/') != -1

def get_content(tag):
    carousel = False
    if tag.name == 'img' and tag.parent.has_attr('class'):
        for class_item in tag.parent['class']:
            if class_item == 'carousel-item':
                carousel = True
    image = False
    if tag.name == 'img' and tag.parent.has_attr('class'):
        for class_item in tag.parent['class']:
            if class_item == 'all-m':
                image = True
    video = tag.name == 'source' and tag.parent.name == 'video'
    return carousel or image or video

user = 'theweeknd'
num_posts = 10

print('Booting up...')
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('/mnt/c/Users/brian/chromedriver_win32/chromedriver.exe', options=options)
driver.get('https://imgtagram.com/u/' + user)
last_height = 0
"""
for i in range(1,100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
"""
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
print("Getting anchor tags...")
links = soup.find_all(is_photo_link)
print("Finished getting anchor tags.")
hrefs = []
print("Getting links from anchor tags...")
for link in links:
    print("Got " + link.get('href'))
    hrefs.append(link.get('href'))
print("Finished getting links.")
post_sources = []
i = 0
print("Getting posts...")
for href in hrefs:
    print("Getting post from " + href)
    if i > num_posts:
        break
    driver.get('https://imgtagram.com' + href)
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    post_sources.append(driver.page_source)
    i = i + 1
print("Finished getting posts.")
print("Getting content...")
content = []
for post_source in post_sources:
    soup = BeautifulSoup(post_source, 'html.parser')
    content_tags = soup.find_all(get_content)
    for content_tag in content_tags:
        content.append(content_tag.get('src'))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(content)
    
driver.close()