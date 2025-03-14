import requests
import threading
import time
import json
from concurrent.futures import ThreadPoolExecutor
from config.config import *
from core.db import RedisClient
import logging

logger = logging.getLogger(__name__)

class ProxyTester:
    def __init__(self):
        self.redis = RedisClient()
        
    def test_proxy(self, proxy):
        """测试单个代理"""
        for test_url in TEST_URLS:
            try:
                proxies = {
                    'http': f'http://{proxy}',
                    'https': f'http://{proxy}'
                }
                response = requests.get(
                    test_url,
                    proxies=proxies,
                    timeout=TEST_TIMEOUT
                )
                if response.status_code == 200:
                    self.redis.add_good_proxy(proxy)
                    return True
            except:
                pass
        self.redis.add_bad_proxy(proxy)
        return False

    def batch_test(self, proxy_list):
        """批量测试代理"""
        with ThreadPoolExecutor(max_workers=TEST_THREAD_COUNT) as executor:
            executor.map(self.test_proxy, proxy_list)

    def start_consuming(self):
        """开始消费测试队列"""
        logger.info('开始消费测试队列...')
        while True:
            # 阻塞式获取队列消息,超时时间1秒
            message = self.redis.db.brpop(REDIS_QUEUE_TEST, timeout=1)
            if message:
                try:
                    proxy = json.loads(message[1])['proxy']
                    self.test_proxy(proxy)
                except Exception as e:
                    logger.error(f"处理代理测试消息失败: {str(e)}")
            time.sleep(0.1)  # 避免CPU占用过高

    def schedule_retest(self):
        """定时重新测试代理"""
        while True:
            # 测试好代理
            good_proxies = self.redis.get_good_proxies()
            if good_proxies:
                # 将好代理重新放入测试队列
                for proxy in good_proxies:
                    # 检查代理是否已经在队列中
                    if not self.redis.db.lpos(REDIS_QUEUE_TEST, json.dumps({'proxy': proxy})):
                        self.redis.db.lpush(REDIS_QUEUE_TEST, json.dumps({'proxy': proxy}))
            time.sleep(GOOD_PROXY_CHECK_INTERVAL)

            # 测试坏代理
            bad_proxies = self.redis.get_bad_proxies()
            if bad_proxies:
                # 将坏代理重新放入测试队列
                for proxy in bad_proxies:
                    # 检查代理是否已经在队列中
                    if not self.redis.db.lpos(REDIS_QUEUE_TEST, json.dumps({'proxy': proxy})):
                        self.redis.db.lpush(REDIS_QUEUE_TEST, json.dumps({'proxy': proxy}))
            time.sleep(BAD_PROXY_CHECK_INTERVAL) 