# _*_ coding : utf-8 _*_
# @Time : 2023/2/12 16:18
# @Author : yangliuan
# @File : 057_get请求的quote
# @Project : python爬虫

# https://www.baidu.com/s?wd=%E8%B5%B5%E9%9B%B7

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

name = "赵雷"

url = url + urllib.parse.quote(name)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode()

print(content)
