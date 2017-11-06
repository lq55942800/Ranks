#coding=utf-8

import http.cookiejar
from urllib import request,parse


#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie1.txt'
values = {"login_name": "cs9001","password": "111111","label":"useonline-gold"}
data = parse.urlencode(values).encode(encoding="utf-8")
url = "http://172.16.88.165/api/user/login"
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent}
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
#利用request库的HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = request.build_opener(handler)
#创建请求
req = request.Request(url, data, headers)
#创建一个请求，原理同urllib2的urlopen
response = opener.open(req)
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
page = response.read()
print (page)