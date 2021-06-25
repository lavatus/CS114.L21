# -*- coding: utf-8 -*-
"""NBCNews.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HXv7kueR5PrmmKKLuA__9lQKatPsisOM
"""

import requests
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm # để theo dõi tiến trình
import json
data_NBC = []
def getData(URL):
    count = 0
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    getMonth = soup.find("main", class_ = "MonthPage")
    Month = getMonth.findAll("a")
    for i in Month:
        data_NBC.append({                           
                'article_link': i.get("href"),
                'headline': i.text,
                'is_sarcastic': 0})
        count+= 1
    return count

arr_url =[]
month =  ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november','december',]
def sendRequest(year, month):
    count = 0
    for i in range(1,3): # Vì mỗi năm được chia làm 2 trang: 6 tháng đầu và 6 tháng sau
        if (i==1):
            url = 'https://www.nbcnews.com/archive/articles/' + str(year) + '/' + month
        if (i==2):
            url = 'https://www.nbcnews.com/archive/articles/' + str(year) + '/' + month + '/' + str(i)
        arr_url.append(url)
        count += getData(url)
    return count


# crawl

count = 0
for year in tqdm(range(2019,2021), desc = 'year'):
    for m in month:
        count+= sendRequest(year,m)
for m in range(5):
    count+= sendRequest(2021,month[m])
print("Crawled:", count)

with open('NBCNews.json', 'w') as f:
    json.dump(data_NBC, f, indent=3)
print('Done')