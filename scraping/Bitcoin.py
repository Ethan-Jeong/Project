from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import sqlite3

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://kr.investing.com/crypto/bitcoin/historical-data')
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
conn = sqlite3.connect('Bitcoin_crawling.db', isolation_level=None)

with conn:
    cur = conn.cursor()
    create_table ="""
                    drop table if exists Bitcoin;
                    create table Bitcoin(
                        bit_date text,
                        bit_price real,
                        bit_open real,
                        bit_high real,
                        bit_low real,
                        bit_vol real,
                        bit_change real
                    );
    
    """
    cur.executescript(create_table)
data_list = soup.select('#curr_table > tbody > tr')
bitcoin_list = []
for data in data_list:
    date = data.select('td')[0].text.strip()
    price =  data.select('td')[1].text.strip()
    open = data.select('td')[2].text.strip()
    high = data.select('td')[3].text.strip()
    low = data.select('td')[4].text.strip()
    vol = data.select('td')[5].text.strip()
    change = data.select('td')[6].text.strip()
    insert_data = "insert into Bitcoin(bit_date, bit_price, bit_open, bit_high, bit_low, bit_vol, bit_change) values(?, ?, ?, ?, ?, ?, ?)"
    cur.execute(insert_data, (date, price, open, high, low, vol, change))
    bitcoin_list.append([date, price, open, high, low, vol, change])
    columns = ['날짜', '종가', '오픈', '고가', '저가', '거래량', '변동%']
    result = pd.DataFrame(bitcoin_list, columns = columns)
    result.to_excel('C:/Develops/project/files/Bitcoin_crawling.xlsx', index=False)
    conn.commit()
driver.close()
driver.quit()