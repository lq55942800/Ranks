#coding=utf-8

import requests
import re

URL = 'https://book.douban.com/'
response = requests.get(URL).text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
result = re.findall(pattern,response)
for i in result:
    url,name,author,date = i
    author = re.sub('\s','',author)
    date = re.sub('\s','',date)
    print(url,name,author,date)