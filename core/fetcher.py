import requests
from config.config import *
from core.db import RedisClient
import logging
import json

logger = logging.getLogger(__name__)

class ProxyFetcher:
    def __init__(self):
        self.redis = RedisClient()
        
    def fetch_proxies(self, proxy_source_url):
        try:
            proxies = {
                "http": "http://127.0.0.1:10809",
                "https": "http://127.0.0.1:10809",
            }
            
            response = requests.get(proxy_source_url, proxies=proxies, timeout=10)
            if response.status_code == 200:
                proxy_list = set()  # 使用set进行去重
                for line in response.text.split('\n'):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        proxy_list.add(line)
                
                if proxy_list:
                    # 过滤掉已经在各个集合中的代理
                    existing_proxies = set()
                    existing_proxies.update(self.redis.get_all_proxies())
                    existing_proxies.update(self.redis.get_good_proxies())
                    existing_proxies.update(self.redis.get_bad_proxies())
                    
                    # 只处理新代理
                    new_proxies = proxy_list - existing_proxies
                    
                    if new_proxies:
                        # 发送到测试队列
                        for proxy in list(new_proxies):
                            self.redis.db.lpush(REDIS_QUEUE_TEST, json.dumps({'proxy': proxy}))
                        logger.info(f"获取到{len(proxy_list)}个代理，新增{len(new_proxies)}个到测试队列")
                        return True
                    else:
                        logger.info("没有新的代理需要测试")
        except Exception as e:
            logger.error(f"获取代理失败: {str(e)}")
        return False 