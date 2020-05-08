# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    timestamp=models.DateTimeField()
    class Meta:
        ordering=('-timestamp',)

class Crawl_article(models.Model):
    link=models.TextField()
    title=models.CharField(max_length=50)
    body=models.TextField()
    date=models.DateField()
class SelfInformation(models.Model):
    industry=models.CharField(max_length=50)
    workcity=models.CharField(max_length=30)
    education_background=models.CharField(max_length=30)
    sex=models.CharField(max_length=10)
    experience=models.CharField(max_length=30)
    job_form=models.CharField(max_length=30)
    company_form=models.CharField(max_length=30)
    kill=models.CharField(max_length=50)



