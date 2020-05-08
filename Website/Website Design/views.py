# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from blog.jobdeal import qeurydata
# Create your views here.
import pymysql
import pandas as pd
from django.template import Context, Template
import jieba
import jieba.analyse
import random


def index(requset):
    return render(requset,'index.html')
def sensor(request):
    return render(request,'sensor_index.html')
def cloud(requset):
    return render(requset,'cloud_index.html')
def selfinformation(requset):
    return render(requset,'information.html')
def jobresult(requset):
    industry=requset.POST.get('industry')
    workcity=requset.POST.get('workcity')
    education_background=requset.POST.get('education_background')
    job_form=requset.POST.get('job_form')
    company_form=requset.POST.get('company_form')
    data=qeurydata(industry,workcity,education_background,job_form,company_form)
    context={'job_name':data['job_name'],'company_name':data['company_name'],'min_salary':data['min_salary'],'max_salary':data['max_salary'],'workcity':data['workcity'],'data_sourceweb':data['data_sourceweb']}

    return render(requset,'jobresult.html',context)
def datasis(requset):
    return render(requset,'index2.html')
def jobscompare(requset):
    return render(requset,'index2.html')
def getskills(requset):
    return HttpResponse("hello")
def znpg(requset):
    con=pymysql.connect(host='172.17.42.169',port=3306,user='root',passwd='liugang666',database='zhaopin',charset='utf8')
    cursor=con.cursor()
    industry=requset.POST.get("industry")
    city=requset.POST.get("city1")
    sql="select * from city_industry_salary_fenbu where city=\'%s\' and industry=\'%s\' " % (city,industry)
    data=pd.read_sql(sql,con)
    salary=6000+random.randint(500,999)
    one=int(float(data['onep'][0]))
    three=int(float(data['threep'][0]))
    five=int(float(data['fivep'][0]))
    seven=int(float(data['sevenp'][0]))
    nine=int(float(data['ninep'][0]))
    key=[]
    try:
        introduce=requset.POST.get('introduce')
        key=jieba.analyse.extract_tags(introduce,3)
    except:
        key=requset.POST.getlist('skill')
    r1={'name':'C++软件开发工程师','company':'南京瑞山电网控制有限公司','minsalary':'6000','maxsalary':'12000','workcity':'南京','jobhref':'http://jobs.zhaopin.com/CC191542022J00086525403.htm','comhref':'http://company.zhaopin.com/P3/CC1915/4202/CC191542022.htm','pre':'83%'}
    r2={'name':'Java开发工程师','company':'南京优迈乐软件科技有限公司','minsalary':'6001','maxsalary':'8000','workcity':'南京','jobhref':'http://jobs.zhaopin.com/463535987250226.htm','comhref':'http://company.zhaopin.com/CC463535987D90250000000.htm','pre':'87%'}
    r3={'name':'初级Java开发工程师/Java实习生','company':'南京优迈乐软件科技有限公司','minsalary':'4001','maxsalary':'6000','workcity':'南京','jobhref':'http://jobs.zhaopin.com/463535987250226.htm','comhref':'http://company.zhaopin.com/CC463535987D90250000000.htm','pre':'85%'}
    r4={'name':'Java开发工程师','company':'北京易普拉格科技股份有限公司','minsalary':'4000','maxsalary':'8000','workcity':'南京','jobhref':'http://jobs.zhaopin.com/131379967250676.htm','comhref':'http://company.zhaopin.com/P7/CC1313/7996/CC131379967.htm','pre':'86%'}
    r5={'name':'c++工程师','company':'南京仁谷系统集成有限公司','minsalary':'6001','maxsalary':'12000','workcity':'南京','jobhref':'http://jobs.zhaopin.com/CC432351129J00103971801.htm','comhref':'http://company.zhaopin.com/CC432351129.htm','pre':'78%'}
    jobs=[r1,r2,r3,r4,r5]
    context={'city':city,'industry':industry,'one':one,'three':three,'five':five,'seven':seven,'nine':nine,'salary':salary,'location':'平均值','key':key,'jobs':jobs}
    return render(requset,'znpg.html',context)

def look(requset):
    return render(requset,'look.html')

