# -*- coding: utf-8 -*-
"""
@author: pawe2
"""
#import libraries
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time
import pandas as pd
from bs4 import BeautifulSoup

#assigne url
url = 'xxx'
base_url = 'yyy'
driver = Driver('chrome', headed = False)
driver.get(url)
time.sleep(12)

#accept cookies 
accept_cookies = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/button[2]")
accept_cookies.click()
time.sleep(10)

#reject subscribe offer
try:
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[17]/div/div[2]/div/div/div/div/div/button")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()
except TimeoutException:
    print("The button was not found on the page within the timeout period.")
time.sleep(5)

#reject another subscribe offer
button2 = driver.find_element(By.XPATH, "/html/body/div[18]/div/div[2]/div/div/div/div/div/button")
button2.click()
time.sleep(5)

#show all products on the website 
all_elem = driver.find_element(By.XPATH, "/html/body/div[10]/header/div[3]/div/div/div[1]/div[1]/span[2]/a/span")
all_elem.click()
time.sleep(2)

#parse HTML
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
products_info = []

# check the number of pages with products
number_of_pages = soup.find_all("span", {"class": "page-options"})[0]
number_of_pages = int(number_of_pages.select('a')[-1].get_text())

# go throught the available pages
for page_no in range(1, number_of_pages + 1):
        #just in case of some error  
        try:
            next_page_url = base_url + str(page_no)
            driver.get(next_page_url)
            print('Current page:', next_page_url)
            time.sleep(random.randint(4, 8))
            
            # convert html to BS
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            #collect info about products
            products = soup.find_all("div", {"class": "product-listing-column"})
            for product in products:
                
                #create empty dictionary
                data = {}
                product_name = product.find("div", {"class": "product-name"}).a['title']
                product_code = product.find("div", {"class": "product-code"}).get_text()
                try:
                    stock_status = product.find("div", {"class": "product-availability"}).get_text()
                except:
                    stock_status = "NONE"
                    print('No stock status info')
                product_prices = product.find("div", {"class": "product-prices"}).get_text()
                try:
                    product_url1 = product.find("div", {"class": "product-name"}).a['href']
                    product_url = "zzz" + product_url1
                except:
                    product_url = "NONE"
                    print('No product_url info')
                
                #put data into dictionary
                data['product_name'] = product_name
                data['product_code'] = product_code
                data['product_prices'] = product_prices.strip()
                data['product_url'] = product_url
                data['stock_status'] = stock_status
                products_info.append(data)
                
        except Exception as err:
            print(f'Error on page {page_no}')
            print(err)

#create dataframe
df = pd.DataFrame(products_info)
print(df)

#convert to excel
#df.to_excel(xxxx)
   
