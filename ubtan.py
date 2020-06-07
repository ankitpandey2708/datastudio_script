import locale
locale.setlocale( locale.LC_ALL,"en_US.UTF-8")
import time
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://datastudio.google.com/u/0/reporting/1Ls-fZUS6nw8NyY5jEpjW1XB5a1mADr56/page/k7Xn'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
elem = driver.page_source.encode('utf-8')
html_soup = BeautifulSoup(elem, 'html.parser')
a=html_soup.find_all('div', {'class': 'valueLabel ng-binding'})
Impressions = int(a[0].text.split()[0].replace(',',''))
Clicks = int(a[1].text.split()[0].replace(',',''))
print(Impressions)
print(Clicks)
