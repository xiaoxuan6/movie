import os

import requests as re
from dotenv import find_dotenv, load_dotenv
from lxml import etree

load_dotenv(find_dotenv())
domian = os.environ.get('HZZ_URL')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}


def crawling(keyword: str, num: int):
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

    # 遍历结果筛选选集
    return get_anthology_url(item[0], num)


def get_anthology_url(url: str, num: int):
    html_data = re.get(url, headers=header).text
    sub_tree = etree.HTML(html_data)

    anthology = f'第 {num} 集'
    data = sub_tree.xpath('//div[@class="stui-pannel_bd col-pd clearfix"]/ul/li//text()')
    if anthology in data:
        target = sub_tree.xpath(f'//div[@class="stui-pannel_bd col-pd clearfix"]/ul/li[{num}]//@href')
        if len(target) > 0:
            return True, domian + target[0]
    else:
        return False, f'搜索结果中不包含选集{num}'
