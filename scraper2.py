# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:57:00 2024

@author: pawe2
"""
import selenium
from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup
import pandas as pd

lower_time_page = 5
upper_time_page = 10 

url = 'xxxx'
driver = Driver(browser='chrome', headed = False)
driver.get(url)
time.sleep(random.randint(lower_time_page, upper_time_page))
accept_cookies = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]/div[1]/button' )
accept_cookies.click()
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(random.randint(lower_time_page, upper_time_page))
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
time.sleep(1)

products = soup.find_all("div", {"class": "product-listing-column"})
products_info = []

for product in products:
    data = {}
    poduct_name = product.find("div", {"class": "product-name"}).a['title']
    product_code = product.find("div", {"class": "product-code"})
    my_id = product_code.find(class_ = "value").get_text()
    try:
        stock_status = product.find("div", {"class": "stock-check"}).get_text()
    except:
        stock_status = "NONE"
        print('No stock status info')
    product_prices = product.find("div", {"class": "product-prices"})
    price = product_prices.get_text()
    try:
        product_url = product.find("div", {"class": "product-name"}).a['href']
        product_url = "zzzz" + product_url
    except:
        product_url = "NONE"
        print('No product_url info')
    data['poduct_name'] = poduct_name
    data['my_id'] = my_id
    data['stock_status'] = stock_status
    data['price'] = price.strip()
    data['product_url'] = product_url
    products_info.append(data)
   
df = pd.DataFrame(products_info)
df.to_excel(r"yyyy", sheet_name='project')

