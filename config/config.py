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

# RabbitMQ配置
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')

# 队列名称
QUEUE_FETCH = 'proxy_fetch'
QUEUE_TEST = 'proxy_test'

# 代理源配置
PROXY_SOURCES = [
    #'https://raw.githubusercontent.com/gitrecon1455/ProxyScraper/refs/heads/main/proxies.txt',
    'https://github.com/Zaeem20/FREE_PROXIES_LIST/raw/master/http.txt'
]

# 测试目标URL
TEST_URLS = [
    'http://www.baidu.com',
    'http://app-cdn.jjwxc.net',
]

# 测试配置
TEST_TIMEOUT = 1
GOOD_PROXY_CHECK_INTERVAL = 5 * 60  # 5分钟
BAD_PROXY_CHECK_INTERVAL = 1 * 60 * 60  # 1小时
TEST_BATCH_SIZE = 100
TEST_THREAD_COUNT = 20 