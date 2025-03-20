import redis
from config.config import *
import logging
import random
import time


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
        # 设置代理的过期时间为5小时
        expire_time = int(time.time()) + 60* 60 * 5
        self.db.hset(f'{REDIS_KEY_BAD_PROXIES}_expire', proxy, expire_time)
        self.db.expireat(f'{REDIS_KEY_BAD_PROXIES}_expire', expire_time)

    def is_proxy_expired(self, proxy):
        """检查代理是否已过期"""
        expire_time = self.db.hget(f'{REDIS_KEY_BAD_PROXIES}_expire', proxy)
        if expire_time and int(expire_time) < int(time.time()):
            return True
        return False

    def clean_expired_proxies(self):
        """清理过期的 bad proxy"""
        while True:
            try:
                cnt = 0
                for proxy in self.db.smembers(REDIS_KEY_BAD_PROXIES):
                    if self.is_proxy_expired(proxy):
                        cnt +=1
                        self.db.srem(REDIS_KEY_BAD_PROXIES, proxy)
                        self.db.hdel(f'{REDIS_KEY_BAD_PROXIES}_expire', proxy)
                if cnt > 0 :
                    logger.info(f"删除{cnt}个过期的无效key")
            except Exception as e:
                logger.error(str(e))
            time.sleep(30)
    
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
    redis_client = RedisClient()
    redis_client.clear()
    pass