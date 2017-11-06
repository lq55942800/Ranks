#coding=utf-8

from urllib import request
import http.cookiejar


#cookie已经存在'cookie.txt'，提取cookie，见cookieLog.py

#创建MozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
handler = request.HTTPCookieProcessor(cookie)
req = request.Request("http://www.baidu.com")
opener = request.build_opener(handler)
response = opener.open(req)

