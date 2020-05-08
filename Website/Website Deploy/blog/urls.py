# -*- coding: utf-8 -*-
from django.conf.urls import url,include
import blog.views

urlpatterns=[ url(r'^$', blog.views.index),
	      url(r'^sensor/$',blog.views.sensor),
	      url(r'^cloud_index/$',blog.views.cloud),
              url(r'^selfinformation/$',blog.views.selfinformation),
              url(r'^jobresult/$',blog.views.jobresult),
              url(r'^data_analysis/$',blog.views.datasis),
              url(r'^jobscompare/$',blog.views.jobscompare),             
              ]


