#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import pymysql
import numpy as np
import pandas as pd

def conmysql():    
    conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        database='zhaopin',
        charset='utf8',
    )
    return conn

def qeurydata(industry,workcity,education_background,job_form,company_form):
    conn=conmysql()
    cursor=conn.cursor()
    qeurysql='select job_name,company_name,min_salary,max_salary,workcity,data_sourceweb from collect2 where  company_industry='+'"'+industry+'"'+' and workcity='+'"'+workcity+'"'+' and education_background='+'"'+education_background+'"'+' and job_form='+'"'+job_form+'"'+' and company_form='+'"'+company_form+'"'+' order by salary desc limit 10;'
    data=pd.read_sql(qeurysql,conn)
    return data

if __name__ == '__main__':
    industry="'计算机软件'"
    workcity="'北京'"
    education_background="'本科'"
    job_form="'全职'"
    company_form="'民营'"
    data1=qeurydata(industry,workcity,education_background,job_form,company_form)
    print 'read ok'
    print data1

    print 'ok'

