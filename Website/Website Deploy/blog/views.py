# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from blog.jobdeal import qeurydata
# Create your views here.


def index(requset):
    return render(requset,'index.html')
def sensor(request):
    return render(request,'sensor_index.html')
def cloud(requset):
    return render(requset,'cloud_index.html')
def selfinformation(requset):
    return render(requset,'selfinformation.html')
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
    return render(requset,'index.html')
def jobscompare(requset):
    return render(requset,'index.html')


