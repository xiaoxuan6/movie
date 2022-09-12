import os

import requests as re
from dotenv import find_dotenv, load_dotenv
from lxml import etree

load_dotenv(find_dotenv())
domian = os.environ.get('HZZ_URL')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}


def crawling(keyword: str):
    content = re.get(f'{domian}/search?q={keyword}', headers=header).text
    tree = etree.HTML(content)

    # 查找所有的搜索结果
    lis = tree.xpath('//div[@class="stui-pannel_bd"]/ul/li')
    item = []
    for li in lis:
        result = li.xpath('//a[@class="stui-vodlist__thumb lazyload"]/@href')
        if result:
            item.append(f'{domian}{result[0]}')

    if len(item) == 0:
        return False, '搜索结果为空'

    return True, item[0]
