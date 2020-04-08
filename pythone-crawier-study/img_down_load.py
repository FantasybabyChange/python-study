url = "http://www.cnu.cc/works/396609"
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
from bs4 import BeautifulSoup
import requests
import os
import shutil


# 只能去拉去静态网页
def download(url, download_path):
    response = requests.get(url, stream=True)
    print(response.status_code)
    if response.status_code == 200:
        print(download_path)
        with open(download_path, "wb") as file:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, file)


def img_download(url):
    response = requests.get(url, headers=headers)
    content = BeautifulSoup(response.text, 'lxml')
    find_all = content.find_all("thumbnail", class_="thumbnail")
    for img in find_all:
        img_url = img.get("src")
        print(img.get("src"))
        abspath = os.path.abspath('.')
        fileName = os.path.basename(img_url)
        ab_file_name = os.path.join(abspath, fileName)
        # download(img_url, ab_file_name)
        print("start down load")


img_download(url)
