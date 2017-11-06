#coding=utf-8

import requests,json
from urllib.parse import urlencode
from requests.exceptions import RequestException


def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
    }
    url = 'http://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求失败。')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def main():
    html = get_page_index(0,'手机').encode('utf-8').decode('unicode_escape')
    print(type(html))
    # for url in parse_page_index(html):
    #     # print(url)


if __name__ == '__main__':
    main()
