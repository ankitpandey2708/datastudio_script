import time
from selenium import webdriver
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get("https://datastudio.google.com/u/0/reporting/1Ls-fZUS6nw8NyY5jEpjW1XB5a1mADr56/page/k7Xn")
time.sleep(5)
elem = driver.page_source.encode('utf-8')
html_soup = BeautifulSoup(elem, 'html.parser')
a=html_soup.find_all('div', {'class': 'valueLabel'})
Impressions = int(a[0].text.split()[0].replace(',',''))
Clicks = int(a[1].text.split()[0].replace(',',''))
print(Impressions)
print(Clicks)