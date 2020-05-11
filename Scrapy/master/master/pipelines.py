# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import redis
from scrapy_redis.spiders import RedisSpider

class MasterPipeline(object):
    '''
    def __init__(self,host,port):
        
        #连接redis数据库
        #self.redis_url = 'redis://password:@localhost:6379/'  
        #self.r = redis.Redis.from_url(self.redis_url,decode_responses=True)  

    '''
    def __init__(self,host,port):
        #连接redis数据库
        self.r = redis.Redis(host=host, port=port,decode_responses=True)
        #self.redis_url = 'redis://password:@localhost:6379/'  
        #self.r = redis.Redis.from_url(self.redis_url,decode_responses=True)  

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get("REDIS_HOST"),
            port = crawler.settings.get("REDIS_PORT"),
        )

    def process_item(self, item, spider):
        self.r.lpush('spider_index:start_urls', item['url'])