#/bin/python
import requests
url="http://www.doutula.com/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',}
res = requests.get(url,headers=headers)
import lxml
from lxml import etree

html = etree.HTML(res.text)
srcs = html.xpath('.//img/@data-original')
for src in srcs:
    filenam = src.split('/')[-1]
    print(src, filenam)
print(len(srcs))