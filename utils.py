import time
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup
from requests import RequestException


def log(*args, **kwargs):
    is_show = kwargs.pop('is_show', False)
    val = time.localtime()
    standard_time = time.strftime("%Y-%m-%d %H:%M:%S", val)
    with open('log.txt', 'a', encoding='utf-8') as f:
        if is_show:
            print('"{}" '.format(standard_time), *args, **kwargs)
        else:
            print('"{}" '.format(standard_time), *args, **kwargs, file=f)


def joint_url(*args, **kwargs):
    """
    通过host, path, data拼装出url
    :return: 完整的url
    """
    host = kwargs.get('host', '')
    path = kwargs.get('path', '')
    data = kwargs.get('data', {})
    params = urlencode(data)
    url = ''.join((host, path, '?', params))
    return url


def get_html(url):
    html = ''
    if url == '':
        pass
    else:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html = response.text
        except RequestException as e:
            log('error', e)
    return html


def html_title(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    return title


def image_url(image_id):
    url = 'http://p1.pstatp.com/origin/{}'.format(image_id)
    return url
