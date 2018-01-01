import re

ENTRANCE = dict(
    host=r'https://www.toutiao.com',
    path=r'/search_content/',
)

ENTRANCE_DATA = {
    'format': 'json',
    'autoload': True,
    'count': 20,
    'cur_tab': 3,
    'from': 'gallery',
}

IMAGES_ID_PATTERN = re.compile(r'origin\\\\\/(.*?)\\', re.S)

SEARCH_KEYWORDS = '街拍'

MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'

