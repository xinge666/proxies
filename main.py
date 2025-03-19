import threading
from core.fetcher import ProxyFetcher
from core.tester import ProxyTester
from api.proxy_api import run_api
from config.config import PROXY_SOURCES
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def run_fetcher():
    fetcher = ProxyFetcher()
    while True:
        for url in PROXY_SOURCES:
            print(url)
            fetcher.fetch_proxies(url)
        time.sleep(3600)  # 每小时获取一次

def run_tester():
    tester = ProxyTester()
    # tester.start_consuming()
    # 启动消费者线程
    print('启动消费者线程')
    consumer_thread = threading.Thread(target=tester.start_consuming)
    consumer_thread.daemon = True
    consumer_thread.start()
    print('启动重测线程')
    # 启动重测线程
    retest_thread = threading.Thread(target=tester.schedule_retest)
    retest_thread.daemon = True
    retest_thread.start()

    #启动重测低质线程（必要性存疑）
    retest_thread = threading.Thread(target=tester.schedule_retest_bad)
    retest_thread.daemon = True
    retest_thread.start()
    

if __name__ == '__main__':
    from core.db import RedisClient

    redis_client = RedisClient()
    redis_client.clear()
    # # 启动获取器
    fetcher_thread = threading.Thread(target=run_fetcher)
    fetcher_thread.daemon = True
    fetcher_thread.start()

    # 启动测试器
    tester_thread = threading.Thread(target=run_tester)
    tester_thread.daemon = True
    tester_thread.start()

    # # 启动API服务
    run_api() 