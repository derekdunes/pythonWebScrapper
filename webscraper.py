from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from  bs4 import BeautifulSoup
#import pandas as pd

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://scholarship-positions.com/inti-postgraduate-merit-international-scholarship-in-malaysia/2019/10/18/")
content = driver.page_source
print(content)




# soup = BeautifulSoup(content)
# scholarTitle = soup.find('div', attrs={'class':'entry-title'})

# print(scholarTitle)
