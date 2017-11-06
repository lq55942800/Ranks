#coding=utf-8

#import urllib.request,urllib.parse
import http.cookiejar
from urllib import request,parse


url = "http://www.qiushibaike.com/"
user_agent="User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4)"
header = { 'User-Agent' : user_agent}
data = None
req = request.Request(url,data,header)
response = request.urlopen(req)
page = response.read().decode('utf-8')
print (page)



