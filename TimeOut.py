#coding=utf-8

from urllib import request,error,parse
import socket

try:
    response = request.urlopen('http://wwww.baidu.com',timeout=0.1)
    print(type(response),response.status,response.getheader('Date'))
    print(response.getheaders())
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("Time Out.")

    re = parse.urlencode()