#coding=utf-8

import http.cookiejar
from urllib import request


#声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
#通过request.HTTPCookieProcessor创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = request.build_opener(handler)
#此处的open方法同request的urlopen方法，也可以传入Request
response = opener.open("http://www.hao123.com/")
for item in cookie:
    print ('Name = '+item.name)
    print ('Values = ' + item.value)
