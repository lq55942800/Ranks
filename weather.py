#coding=utf-8

import requests,json,sys,time

def get_weather():
    city = '上海'
    URL = "http://www.sojson.com/open/api/weather/json.shtml?city=%s"%city
    response = requests.get(URL)
    response.encoding='utf-8'
    print(response.text)
    # response_json_encode = json.dumps(response.text)
    # response_json_decode = json.loads(response_json_encode)
    # print(response_json_decode)
    return response.text

def write_file(text):
    with open("/Users/刘强/test.txt",'w+') as file:
        file.write(text)

if __name__ == '__main__':
    response = get_weather()
    write_file(response)



