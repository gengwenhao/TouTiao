import json
import re
from json import JSONDecodeError

import pymongo

import utils
from config import (
    ENTRANCE,
    ENTRANCE_DATA,
    IMAGES_ID_PATTERN,
    SEARCH_KEYWORDS,
    MONGO_URL,
    MONGO_DB,
    MONGO_TABLE
)

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def entrance_result(offset, keyword):
    """
    入口页面的返回结果
    """
    data = {
        'offset': offset,
        'keyword': keyword,
    }
    data.update(ENTRANCE_DATA)
    ENTRANCE['data'] = data
    url = utils.joint_url(**ENTRANCE)
    html = utils.get_html(url)
    return html


def article_urls(html):
    """
    根据入口页返回结果, 得到的所有文章页面地址
    """
    urls = []
    try:
        data = json.loads(html)
        data = data.get('data', [])
        urls = [item.get('article_url', '') for item in data]
    except JSONDecodeError as e:
        utils.log(e)
    return urls


def article_images_id(html):
    """
    文章页html源码中, 图片的id
    """
    re_list = re.findall(IMAGES_ID_PATTERN, html)
    images_id = list(set(re_list))
    return images_id


def article_detail(article_url):
    """
    访问文章url得到的详细数据
    """
    html = utils.get_html(article_url)
    title = utils.html_title(html)
    images_id = article_images_id(html)
    images_url = [utils.image_url(id) for id in images_id]

    return {
        'title': title,
        'images_url': images_url,
        'article_url': article_url,
    }


def save_to_db(result):
    save_success = False
    save_success = db[MONGO_TABLE].insert(result)
    return save_success


def main(offset, keyword=SEARCH_KEYWORDS):
    results = entrance_result(offset, keyword=keyword)
    art_urls = article_urls(results)
    for art_url in art_urls:
        result = article_detail(art_url)
        success = save_to_db(result)
        message = 'save success' if success else 'save failed'
        utils.log(message, result)


if __name__ == '__main__':
    for i in range(0, 401, 20):
        main(offset=i)
