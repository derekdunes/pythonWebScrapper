from selenium import  webdriver
from  bs4 import BeautifulSoup
#import pandas as pd


driver = webdriver.PhantomJS()

driver.get("https://scholarship-positions.com/inti-postgraduate-merit-international-scholarship-in-malaysia/2019/10/18/")
content = driver.page_source
print(content)




# soup = BeautifulSoup(content)
# scholarTitle = soup.find('div', attrs={'class':'entry-title'})

# print(scholarTitle)
