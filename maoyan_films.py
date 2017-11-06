#coding=utf-8

import requests,re,json
from requests.exceptions import RequestException
from multiprocessing import Pool

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?board-item-main.*?movie-item-info.*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            '排名': item[0],
            '电影名称': item[1],
            '演员': item[2].strip()[3:],
            '上映日期': item[3][5:],
            '得分': item[4]+item[5]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(str(item))
        write_to_file(item)


if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])