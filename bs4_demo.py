#coding=utf-8

from bs4 import BeautifulSoup
import requests
import pyquery

content = requests.get('http://www.baidu.com').text
soup = BeautifulSoup(content,'lxml')
soup.find_next_sibling()