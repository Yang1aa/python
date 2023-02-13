# _*_ coding : utf-8 _*_
# @Time : 2023/2/12 16:34
# @Author : yangliuan
# @File : 058_get请求的urlencode
# @Project : python爬虫

import urllib.request
import urllib.parse

base_url = "https://www.baidu.com/s?"
data = {
    "wd": "赵雷",
    "sex": "男",
    "loaction": "中国内地"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

url = base_url + urllib.parse.urlencode(data)

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
print(content)
