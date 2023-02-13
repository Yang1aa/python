# _*_ coding : utf-8 _*_
# @Time : 2023/2/13 10:53
# @Author : yangliuan
# @File : 061_ajax请求豆瓣电影
# @Project : python爬虫

import urllib.request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

fp = open("douban.json", "w", encoding='utf-8')
fp.write(content)