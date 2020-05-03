# igscraper.py

Script that uses Selenium and BeautifulSoup4 to provide a function to scrape media from an Instagram profile without access to Instagram API,
since getting your app approved by Instagram is too annoying of a process.

## Disclaimer 

This is definitely NOT a perfect scraper. 

Scraping directly from the Instagram website is too tricky and will probably get your IP banned. I took an alternative route by
scraping the media from a Instagram web viewer website called Imgtagram, which seems to be more tolerant of scraping. However,
this does lead to a couple issues:

- Videos in carousels: Videos in carousel posts are not downloaded correctly; they are instead the thumbnail of the video
- IP banning: Imgtagram can ban your IP at any time
- Unpredictability: Imgtagram can change their source code at any time, which will most likely break the scraper

These issues are certainly significant and would make this script totally unsuitable for a large-scale project. However, this script was intended for my personal use and I found my script had a huge advantage in speed over modules that offered similar functionalities (instaloader, instapy, etc.), which was most important to me. Use at your own discretion.


