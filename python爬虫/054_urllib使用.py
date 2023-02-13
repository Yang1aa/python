# _*_ coding : utf-8 _*_
# @Time : 2023/2/12 10:43
# @Author : yangliuan
# @File : 054_urllib使用
# @Project : python爬虫
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
# print(type(response))

# content = response.read()
# 返回多少字节
# content = response.read(5)
# print(content)

# 读取一行
content = response.readline()
print(content)
#
# content = response.readlines()
# print(content)

# 返回状态码 如果是200 那么就证明我们的逻辑没错
print(response.getcode())
# 返回url地址
print(response.geturl())
# 获取状态信息
print(response.getheaders())
