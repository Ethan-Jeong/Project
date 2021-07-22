from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://kr.investing.com/crypto/dogecoin/historical-data')
time.sleep(1)
weekly = driver.find_element_by_css_selector('#data_interval > option:nth-child(2)')
weekly.click()
time.sleep(1)
date = driver.find_element_by_css_selector('#widgetFieldDateRange')
date.click()
time.sleep(1)
start = driver.find_element_by_id('startDate')
start.clear()
start.send_keys('2019/06/09')
end = driver.find_element_by_id('endDate')
end.clear()
end.send_keys('2021/07/04')
date = driver.find_element_by_css_selector('#applyBtn')
date.click()
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data_list = soup.select('#curr_table > tbody > tr')
bitcoin_list = []
for data in data_list:
    date = data.select('td')[0].text.strip()
    fin =  data.select('td')[1].text.strip()
    open = data.select('td')[2].text.strip()
    high = data.select('td')[3].text.strip()
    low = data.select('td')[4].text.strip()
    count = data.select('td')[5].text.strip()
    change = data.select('td')[6].text.strip()
    bitcoin_list.append([date, fin, open, high, low, count, change])
columns = ['날짜', '종가', '오픈', '고가', '저가', '거래량', '변동%']
result = pd.DataFrame(bitcoin_list, columns = columns)
result.to_excel('./files/Dogecoin_crawling.xlsx', index=False)
driver.close()
driver.quit()