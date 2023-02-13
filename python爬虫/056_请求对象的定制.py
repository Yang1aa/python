# _*_ coding : utf-8 _*_
# @Time : 2023/2/12 16:02
# @Author : yangliuan
# @File : 056_请求对象的定制
# @Project : python爬虫

url = "https://www.baidu.com"

import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)
