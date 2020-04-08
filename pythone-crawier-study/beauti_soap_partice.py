url = "https://www.qq.com/?fromdefault"

from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}


def url_get(url):
    get = requests.get(url, headers=headers)
    # print(get.text)
    soup = BeautifulSoup(get.text, "lxml")
    find_all = soup.find_all("div", class_="tab-news")
    # print(find_all)
    for title_href in find_all:
        all_a = title_href.find_all("a")
        # print(all_a)
        for a in all_a:
            if (a.string is not None):
                print(a.string)


url_get(url)
