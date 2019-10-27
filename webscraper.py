from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from  bs4 import BeautifulSoup
#import pandas as pd

#add chrome headless driver for the connection
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

#connect to the url to be scrapped
driver.get("https://scholarship-positions.com/inti-postgraduate-merit-international-scholarship-in-malaysia/2019/10/18/")
content = driver.page_source

#parse the content (html) using beatiful soup 
soup = BeautifulSoup(content, 'html.parser')

#scrape the div containing the content we want
title_box = soup.find('h1', attrs={'class':'entry-title'})

title = title_box.text.strip()

print(title)

detail = soup.find('div', attrs={'class':'entry-content'})

for p in detail.contents: #detail.children detail.descendants
	print(p)


