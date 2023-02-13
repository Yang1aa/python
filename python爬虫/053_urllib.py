# _*_ coding : utf-8 _*_
# @Time : 2023/2/12 10:33
# @Author : yangliuan
# @File : 053_urllib
# @Project : python爬虫

# 使用urllib获取百度网页首页源码
import urllib.request

# 定义一个url 访问地址
url = 'http://www.baidu.com'
# 模拟浏览器向服务器发请求
response = urllib.request.urlopen(url)
# 获取响应中页面源码
# read返回字节型二进制数据

# 将二进制数据转为字符串，解码 decode('编码的格式')
content = response.read().decode('utf-8')

print(content)