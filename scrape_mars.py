# import libraries
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

## NASA Mars Latest News
#desinate source
url = 'https://mars.nasa.gov/news/'
#start hacking
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome',**executable_path,headless=False)
browser.visit(url)

##JPL Mars Space Image
# find the featured image for Mars
url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url1)
# Scrape the image from website
html = browser.html
soup = BeautifulSoup(html,'html.parser')
images = soup.find('a',class_='fancybox')
images.attrs['data-fancybox-href']
featured_image_url = 'https://www.jpl.nasa.gov'+images.attrs['data-fancybox-href']
featured_image_url

## Mars Weather
url2 = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url2)
#Scape weather data
html = browser.html
soup = BeautifulSoup(html,'html.parser')
tweets = soup.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
mars_weather = tweets.contents[0]
mars_weather

##Mars Fact
url3 = 'https://space-facts.com/mars/'
browser.visit(url3)
#Scrape fact data using Pandas
tables = pd.read_html(url3)
tables

## Mars Hemispheres
url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url4)
#Scrape Title and img_src
html = browser.html
soup = BeautifulSoup(html,'html.parser')
results = soup.find_all('div',class_='item')
title = []
img_src = []
for result in results:
    title.append(result.h3.text)
    browser.click_link_by_partial_text(result.h3.text)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    img_src.append('https://astrogeology.usgs.gov'+soup.find('img',class_='wide-image').attrs['src'])
    browser.back()
# zip data into dict.
hemisphere_image_urls=[]
for i in range(0,4):
    hemisphere_image_urls.append({title[i]:img_src[i]})
hemisphere_image_urls