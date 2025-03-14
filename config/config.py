import os

# Redis配置
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_DB = int(os.getenv('REDIS_DB', 0))

# Redis键
REDIS_KEY_ALL_PROXIES = 'proxies:all'
REDIS_KEY_GOOD_PROXIES = 'proxies:good'
REDIS_KEY_BAD_PROXIES = 'proxies:bad'

# Redis队列键
REDIS_QUEUE_TEST = 'queue:proxy_test'  # 测试队列的key


# 代理源配置
PROXY_SOURCES = [
    'https://raw.githubusercontent.com/gitrecon1455/ProxyScraper/refs/heads/main/proxies.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/variableninja/proxyscraper/main/proxies/http.txt',
    'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt',
    'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt',
    'https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/http.txt'

]

# 访问 github 需要代理
PROXY_SOURCES_PROXY = None

PROXY_SOURCES_PROXY = {
                "http": "http://127.0.0.1:10809",
                "https": "http://127.0.0.1:10809",
            }

# 测试目标URL
TEST_URLS = [
    'http://www.baidu.com',
    'http://app-cdn.jjwxc.net',
]

# 测试配置
TEST_TIMEOUT = 1
GOOD_PROXY_CHECK_INTERVAL = 5 * 60  # 5分钟
BAD_PROXY_CHECK_INTERVAL = 1 * 60 * 60  # 1小时
TEST_BATCH_SIZE = 2000
TEST_THREAD_COUNT = 500

