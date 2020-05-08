# -*- coding: utf-8 -*-
import scrapy
from jobs.items import JobsItem
import re
import datetime

class Spider51jobSpider(scrapy.Spider):
    name = 'train_spider_51job'
    allowed_domains = ['jobs.51job.com']
    start_urls = ['http://jobs.51job.com/']

    def parse(self, response):
        #主界面-全部招聘职业
        index_urls = response.xpath("/html/body/div[3]/div[2]//div[@class='lkst']//a/@href").extract()
        #主界面-全部招聘行业
        #index_urls = response.xpath("/html/body/div[3]/div[3]//div[@class='lkst']//a/@href").extract()
        for index_url in index_urls:
            yield response.follow(index_url,self.parse_url)

    def parse_url(self,response):
        job_urls = response.xpath("//span[@class='title']//a//@href").extract()
        for job_url in job_urls:
            yield response.follow(job_url,self.parse_item)

    #parse page
    def parse_item(self,response):
        item = JobsItem()
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
    



