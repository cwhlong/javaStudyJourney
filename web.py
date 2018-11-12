#/bin/python
import requests
import time
import lxml
from lxml import etree
import os
from concurrent import futures

#待访问的网址
url="http://www.doutula.com/"
headers = {
    'Referrer':'http://www.doutula.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',}
res = requests.get(url,headers=headers)


def download_img(src, dirname):
    filename = src.split('/')[-1]
    dirnames = 'imgs/{}'.format(dirname)
    if not os.path.exists(dirnames):
        os.makedirs(dirnames)
    img = requests.get(src, headers=headers)
    with open('{}/{}'.format(dirnames,filename), 'wb') as file:
        file.write(img.content)

def get_page(url):
    time.sleep(0.2)
    resp = requests.get(url, headers=headers)
    dirname = url.split('page=')[-1]
    print(resp, url)
    html = etree.HTML(resp.text)
    srcs = html.xpath('.//img/@data-original')

    ex = futures.ThreadPoolExecutor(max_workers=44)
    for src in srcs:
        ex.submit(download_img, src, dirname)
    next_link = html.xpath('.//a[@rel="next"]/@href')
    return next_link

def main():
    next_link_base = "http://www.doutula.com/article/list/?page="
    current_num = 0
    next_link = ['http://www.doutula.com']
    while next_link:
        time.sleep(0.2)
        current_num += 1
        next_link = get_page(next_link_base + str(current_num))
        if current_num >= 4:
            break

if __name__ == "__main__":
    main()
