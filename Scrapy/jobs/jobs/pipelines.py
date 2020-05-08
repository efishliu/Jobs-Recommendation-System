# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import pymysql
from twisted.internet import defer
import traceback

class JobsPipeline(object):
    def __init__(self):
        dbargs=dict(
            host='127.0.0.1',
            db='job51',
            user='root',
            passwd='LG66zxhy!',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        self.dbpool=adbapi.ConnectionPool('pymysql',**dbargs)


    @defer.inlineCallbacks
    def process_item(self, item, spider):
        try:
            yield self.dbpool.runInteraction(self.insert_into_table,item)
        except:
            print(traceback.format_exc())
        defer.returnValue(item)

    def insert_into_table(self,conn,item):
        #不管数据类型是整数还是字符串，占位符统一用%s
        #mysql_table_name = "all_posts_data"  #全部爬取，使用spider_51job爬虫
        #mysql_table_name = "train_posts_data"   #部分爬取，使用train_spider_51job爬虫
        sql = """INSERT INTO train_posts_data(post_url,post_name,post_salary,post_city,post_experience,post_education,\
        post_number,post_release_time,post_information,post_category,post_keywords,company_url,company_name,\
        company_nature,company_scale,company_category,crawl_date) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""        
        args = (
            item["post_url"],item["post_name"],item["post_salary"],item["post_city"],item["post_experience"],item["post_education"],
            item["post_number"],item["post_release_time"],item["post_information"],item["post_category"],item["post_keywords"],item["company_url"],
            item["company_name"],item["company_nature"],item["company_scale"],item["company_category"],item["crawl_date"]
        )
        conn.execute(sql,args)
        #自动执行conn.commit()

