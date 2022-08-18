#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)






# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
html = browser.html
img_soup = soup(html, 'html.parser')


new = []
for news in img_soup.find_all('a', class_='itemLink product-item'): 
    link = news.get('href')
    if link not in new: 
        new.append(link)
        
# print(new)


# In[53]:


# establish lists 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
html = browser.html
img_soup = soup(html, 'html.parser')
new = []
for news in img_soup.find_all('a', class_='itemLink product-item'): 
    link = news.get('href')
    if link not in new: 
        new.append(link)
        full=[]

# set up the browser 
url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
hemisphere_image_urls = []
links= browser.find_by_css("a.product-item h3")

#create a loop to iterate through the different pages 
for item in range(len(links)):
    hemisphere={}

    # go to the elements by clicking on the link 
    browser.find_by_css("a.product-item h3")[item].click()

    # extract the high resolution image through the sample link 
    img_url= browser.find_link_by_text("Sample").first
    hemisphere['img_url']=img_url['href']

    # get the hemisphere titles 
    hemisphere['title']=browser.find_by_css("h2.title").text

    hemisphere_image_urls.append(hemisphere)

    # Go Back
    browser.back()
    
print(hemisphere_image_urls)







# In[21]:


# 5. Quit the browser
browser.quit()


# In[ ]:




