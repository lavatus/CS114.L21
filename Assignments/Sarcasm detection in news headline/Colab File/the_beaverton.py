# -*- coding: utf-8 -*-
"""The Beaverton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J9l-kWmRQZElUK4mEts4YvqtOnCgRudE
"""

import requests
from bs4 import BeautifulSoup
import json
data = []
# Tờ The Beaverton có headline theo năm/tháng
for year in range(2010,2021):
  for month in range(1,13):
    print(str(month) + '/' +str(year))
    url = "https://www.thebeaverton.com/" + str(year) + "/" + str(month) + "/" 
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html5lib')
    h2 = soup.find_all('h3', {'itemprop': 'headline'}, )
    for link in h2:
        mylink = BeautifulSoup(str(link), 'html.parser')
        gettinglink = mylink.find('a', href=True)
        print(str(gettinglink.find(text=True)))
        data.append({
            'article_link': str(gettinglink['href']),
            'headline': str(gettinglink.find(text=True)),
            'is_sarcastic': 1})
with open('thebeaverton.json', 'w') as f:
    json.dump(data, f, indent=3)
print('Done')

import pandas as pd
data_json = pd.read_json('/content/thebeaverton.json')
data_json