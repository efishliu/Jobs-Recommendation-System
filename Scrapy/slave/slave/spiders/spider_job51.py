# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from slave.items import SlaveItem
import re
import datetime

class SpiderJob51Spider(RedisSpider):
    name = 'spider_job51'
    #allowed_domains = ['example.com']
    #start_urls = ['http://example.com/']
    redis_key = 'spider_index:start_urls'

    def __init__(self, *args, **kwargs):
        # 动态定义allowed_domains
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(SpiderJob51Spider, self).__init__(*args, **kwargs)


    #parse page
    def parse(self,response):
        item = SlaveItem()
        item["post_url"] = response.url
        item["post_name"] = response.xpath("//h1//text()").extract_first()

        #
        
        salary = response.xpath("//div[@class='cn']//strong//text()").extract_first()
        if len(salary) > 0:   
            if salary[-3:] == '万/月':
                min_salary = float(re.findall('(.*?)-(.*?)万',salary)[0][0]) * 10000
                max_salary = float(re.findall('(.*?)-(.*?)万',salary)[0][1]) * 10000
                avg_salary = (min_salary + max_salary) / 2
            elif salary[-3:] == '千/月':
                min_salary = float(re.findall('(.*?)-(.*?)千',salary)[0][0]) * 1000
                max_salary = float(re.findall('(.*?)-(.*?)千',salary)[0][1]) * 1000
                avg_salary = (min_salary + max_salary) / 2
            else:
                avg_salary = 'N'
            item["post_salary"] = float(avg_salary)

        temp = re.sub(r'\xa0','',response.xpath("//*[@class='msg ltype']/@title").extract_first()).split("|")
        if len(temp) >= 5:
            item["post_city"] = temp[0]
            item["post_experience"] = temp[1]
            item["post_education"] = temp[2]
            number = re.findall('招(.*?)人',temp[3])
            if len(number) == 0:
                number = "N"
                item["post_number"] = number
            else:
                item["post_number"] = int(number[0])
            item["post_release_time"] = temp[4]

        item["post_information"] = ''.join(response.xpath("//div[@class='bmsg job_msg inbox']//p//text()").extract()).strip("\n").strip('\r').strip('\t') 
        item["post_category"] = ','.join(response.xpath("//div[@class='mt10']/p[1]//a//text()").extract())
        item["post_keywords"] = ','.join(response.xpath("//div[@class='mt10']/p[2]//a//text()").extract())

        item["company_url"] = response.xpath("//div[@class='com_msg']//a/@href").extract_first() 
        item["company_name"] = response.xpath("//div[@class='com_msg']//a//text()").extract_first()
        item["company_nature"] = response.xpath("//div[@class='com_tag']/p[1]//text()").extract_first()
        item["company_scale"] = response.xpath("//div[@class='com_tag']/p[2]//text()").extract_first()
        item["company_category"] = re.sub(r'[\r\n\s]','',','.join(response.xpath("//div[@class='com_tag']/p[3]//a//text()").extract()))
        
        item["crawl_date"] = datetime.datetime.now().strftime('%Y-%m-%d')
        yield item
