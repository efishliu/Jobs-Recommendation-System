# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位信息
    post_url = scrapy.Field()
    post_name = scrapy.Field()
    post_salary = scrapy.Field()
    post_city = scrapy.Field()
    post_experience = scrapy.Field()
    post_education = scrapy.Field()
    post_number = scrapy.Field()
    post_release_time = scrapy.Field()
    #post_welfare = scrapy.Field()
    post_information = scrapy.Field()
    post_category = scrapy.Field()#所属行业
    post_keywords = scrapy.Field()#职位关键词

    #公司信息
    company_url = scrapy.Field()
    company_name = scrapy.Field()
    company_nature = scrapy.Field()    #企业性质：民营？
    company_scale = scrapy.Field()
    company_category = scrapy.Field()     #企业所属行业

    #管理字段   
    crawl_date = scrapy.Field()
