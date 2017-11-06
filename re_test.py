#coding=utf-8

import re
# 常规匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
def regular_regex():
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
    print(result,'\n',result.group(),'\n',result.span())

# 泛匹配
def normal_regex():
    result = re.match('^Hello.*Demo$',content)
    print(result, '\n', result.group(), '\n', result.span())

# 匹配目标
def target_regex():
    result = re.match('^Hello\s(\d+)\s\w.*Demo$',content)
    print(result, '\n', result.group(1), '\n', result.span())

# 贪婪匹配
def greed_regex():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('He.*(\d+).*Demo$',content)
    print(result, '\n', result.group(1), '\n', result.span())

# 非贪婪匹配
def ungreed_regex():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('He.*?(\d+).*Demo$',content)
    print(result, '\n', result.group(), '\n', result.span())

if __name__ == '__main__':
    ungreed_regex()