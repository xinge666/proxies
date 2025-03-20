import redis
from config.config import *
import logging
import random

logger = logging.getLogger(__name__)

class RedisClient:
    def __init__(self):
        self.db = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            db=REDIS_DB,
            decode_responses=True
        )
    
    def add_proxy(self, proxy):
        """添加代理到待测试集合"""
        return self.db.sadd(REDIS_KEY_ALL_PROXIES, proxy)
    
    def add_good_proxy(self, proxy, score=1):
        """添加可用代理"""
        self.db.zadd(REDIS_KEY_GOOD_PROXIES, {proxy: score})
        self.db.srem(REDIS_KEY_BAD_PROXIES, proxy)
    
    def add_bad_proxy(self, proxy):
        """添加不可用代理"""
        self.db.sadd(REDIS_KEY_BAD_PROXIES, proxy)
        self.db.zrem(REDIS_KEY_GOOD_PROXIES, proxy)
    
    def get_bad_proxies_lenght(self):
        """获取不可用代理数量"""
        return self.db.scard(REDIS_KEY_BAD_PROXIES)
    
    def get_all_proxies_lenght(self):
        """获取所有待测试代理数量"""
        return self.db.scard(REDIS_KEY_ALL_PROXIES)
    
    def get_good_proxies_lenght(self):
        """获取所有可用代理数量"""
        return self.db.zcard(REDIS_KEY_GOOD_PROXIES)

    def get_all_proxies(self):
        """获取所有待测试代理"""
        return self.db.smembers(REDIS_KEY_ALL_PROXIES)
    
    def get_queue_proxies(self):
        return self.db.llen(REDIS_QUEUE_TEST)
    
    
    def get_good_proxies(self):
        """获取所有可用代理"""
        return self.db.zrange(REDIS_KEY_GOOD_PROXIES, 0, -1)
    
    def get_bad_proxies(self):
        """获取所有不可用代理"""
        return self.db.smembers(REDIS_KEY_BAD_PROXIES)
    
    def get_random_good_proxy(self):
        """随机获取一个可用代理"""
        proxies = self.db.zrange(REDIS_KEY_GOOD_PROXIES, 0, -1)
        if proxies:
            return random.choice(proxies)
        return None
    
    def clear(self):
        """删除所有的 REDIS_KEY*"""
        keys = [
            REDIS_KEY_ALL_PROXIES,
            REDIS_KEY_GOOD_PROXIES,
            REDIS_KEY_BAD_PROXIES,
            REDIS_QUEUE_TEST
        ]
        for key in keys:
            if self.db.exists(key):
                self.db.delete(key)

if __name__=="__main__":
    pass