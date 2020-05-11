# -*- coding: utf-8 -*-
import scrapy
from master.items import MasterItem
from scrapy_redis.spiders import RedisSpider

class SpiderIndexSpider(scrapy.Spider):
    name = 'spider_index'
    allowed_domains = ['jobs.51job.com']
    start_urls = ['http://jobs.51job.com/']

    def parse(self, response):
        #主界面-全部招聘职业
        index_urls = response.xpath("/html/body/div[3]/div[2]//div[@class='lkst']//a/@href").extract()
        #主界面-全部招聘行业
        #index_urls = response.xpath("/html/body/div[3]/div[3]//div[@class='lkst']//a/@href").extract()
        for index_url in index_urls:
            yield response.follow(index_url,self.parse_next_url)
    def parse_next_url(self,response):
        #next page
        next_page_url = response.xpath("//li[@class='bk'][2]//a//@href").extract()[0]
        yield response.follow(next_page_url,self.parse_next_url)
        
        job_urls = response.xpath("//span[@class='title']//a//@href").extract()
        for job_url in job_urls:
            yield response.follow(job_url,self.parse_url)

    #return jobs url
    def parse_url(self,response):
        item = MasterItem()
        item["url"] = response.url
        yield item
