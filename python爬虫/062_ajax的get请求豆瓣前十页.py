# _*_ coding : utf-8 _*_
# @Time : 2023/2/13 11:12
# @Author : yangliuan
# @File : 062_ajax的get请求豆瓣前十页
# @Project : python爬虫

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20

import urllib.request
import urllib.parse


def get_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    url = base_url + urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(page, content):
    with open('douban' + str(page) + '.json', "w", encoding='utf-8') as fp:
        fp.write(content)
        fp.close()


if __name__ == '__main__':
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        request = get_request(page)
        content = get_content(request)
        download(page, content)
