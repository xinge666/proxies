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
    #'https://raw.githubusercontent.com/gitrecon1455/ProxyScraper/refs/heads/main/proxies.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/variableninja/proxyscraper/main/proxies/http.txt',
    'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt',
    'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt',
    'https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
    'https://raw.githubusercontent.com/nhan0o22/proxy/master/proxy.txt',
    'https://raw.githubusercontent.com/claude89757/free_https_proxies/main/https_proxies.txt'

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
    #'http://www.yimixs.net/shuku?page=832',
]

TEST_TEXT_FLAG =  '百度'

HEADERS = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
        }

# 测试配置
TEST_TIMEOUT = 5
GOOD_PROXY_CHECK_INTERVAL = 15 * 60  # 5分钟
BAD_PROXY_CHECK_INTERVAL = 24 * 60 * 60  # 1小时
TEST_BATCH_SIZE = 3000
TEST_THREAD_COUNT = 500

