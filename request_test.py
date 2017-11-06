#coding=utf-8

import requests
from requests import exceptions


# data = {'name':'John','age':22}
# response = requests.get('http://www.httpbin.org/get',params = data)
#  response.encoding='utf-8'
# print(requests.codes.ok)

response = requests.get('https://kyfw.12306.cn/otn/',verify=False)
print(response.status_code)
