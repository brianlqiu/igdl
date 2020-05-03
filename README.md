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
- Speed: Waiting for Selenium to load every page and then filtering all of the code can take a pretty long time

This is intended for personal use and possibly for others to use as reference. Use at your own risk.
