#coding=utf-8

# 爬去糗事百科首页，将文字存储为本地txt文件

from urllib import request,parse
import requests
from bs4 import BeautifulSoup
import time

url = 'http://www.qiushibaike.com/'

header = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4)'}

data=None

req = request.Request(url, data, header)

response = request.urlopen(req)

page = response.read().decode('utf-8')

soup = BeautifulSoup(page ,'html.parser')

a = soup.select(".content")

L = []

for i in a:
    L.append(i.text)

file = open('/Users/刘强/Downloads/test.txt','a+')
str_l = ''.join(L)
file.write(str_l)
file.write(time.asctime())

line = '-------------------------------------------------------------------------------------------------'
file.write(line)

file.close()

