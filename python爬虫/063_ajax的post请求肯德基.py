# _*_ coding : utf-8 _*_
# @Time : 2023/2/13 19:31
# @Author : yangliuan
# @File : 063_ajax的post请求肯德基
# @Project : python爬虫

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
import urllib.request
import urllib.parse


def get_request(addr, page):
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        'cname': addr,
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(address, page, content):
    with open("kfc——" + address + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)
        fp.close()


if __name__ == '__main__':
    address = input("请输入查询城市：")
    start_page = int(input("请输入起始页："))
    end_page = int(input("请输入终止页："))
    for page in range(start_page, end_page + 1):
        request = get_request(address, page)
        content = get_content(request)
        download(address, page, content)
