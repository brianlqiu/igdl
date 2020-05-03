from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import re
import pprint
import math

def is_photo_link(tag):
    return tag.name == 'a' and tag.has_attr('href') and tag['href'].find('/m/') != -1

def filter_content(tag):
    carousel = False
    image = False
    if tag.name == 'img' and tag.parent.has_attr('class'):
        for class_item in tag.parent['class']:
            if class_item == 'carousel-item':
                carousel = True
            if class_item == 'all-m':
                image = True
    video = tag.name == 'source' and tag.parent.name == 'video'
    return carousel or image or video

def get_content(user, num_posts):
    #Setup
    print('Booting up...')
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome('/mnt/c/Users/brian/chromedriver_win32/chromedriver.exe', options)
    driver.get('https://imgtagram.com/u/' + user)

    #Scroll
    num_scrolls = math.ceil(num_posts / 12)
    last_height = 0
    for i in range(1,num_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    html_source = driver.page_source

    #Getting anchor tags
    print("Getting anchor tags...")
    soup = BeautifulSoup(html_source, 'html.parser')
    links = soup.find_all(is_photo_link)
    print("Finished getting anchor tags.")

    #Getting post links
    print("Getting post links from anchor tags...")
    hrefs = []
    for link in links:
        print("Got " + link.get('href'))
        hrefs.append(link.get('href'))
    print("Finished getting links.")

    #Getting post source code
    print("Getting posts sources...")
    post_sources = []
    for href in hrefs:
        print("Getting post from " + href)
        driver.get('https://imgtagram.com' + href)
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        try:
            carousel = driver.find_element_by_class_name('carousel-control-next')
            ActionChains(driver).click(carousel).perform()
            time.sleep(0.5)
        except:
            print("Not a carousel.")
        finally:
            post_sources.append(driver.page_source)
    print("Finished getting posts.")

    #Getting content from the source code
    print("Getting content...")
    content = []
    for post_source in post_sources:
        soup = BeautifulSoup(post_source, 'html.parser')
        content_tags = soup.find_all(filter_content)
        for content_tag in content_tags:
            content.append(content_tag.get('src'))
    driver.close()
    return content
    