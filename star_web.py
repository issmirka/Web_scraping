# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:36:47 2024

@author: pawe2
"""
  
import requests
with open (r"C:\Users\pawe2\OneDrive\Pulpit\star.html", 'r') as file:
    html_page = file.read()
    

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_page, 'html.parser')

print(soup.prettify)

page_title =soup.title
print(page_title)

page_title_str = page_title.string
print(page_title_str)

header2 = soup.find('h2')
print(header2)

header1 = soup.find('h1')
print(header1.string)

import re
all_headers = soup.find_all(re.compile('^h[1-2]$'))
paragraphs = soup.find_all('p')
print(paragraphs)
print(paragraphs[4].a['href'])

soup.find('p').text

all_paragraphs = [p.text for p in soup.find_all('p')]
print (all_paragraphs)

soup.select('a')
soup.select_one('h1').text
soup.find('a').find_parent()
soup.find('h1').find_next_sibling()  


