# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtest.views.home', name='home'),
    # url(r'^djtest/', include('djtest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #静态文件
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    
    (r'^file/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.FILE_ROOT}),
    #下载文件
   # (r'^upload/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    
    
     #xls
     url(r'^index/', 'adbweb.views.index'),
      url(r'^ajax/getxy', 'adbweb.views.ajax_getxy'),
      
    #search
    url(r'^search/', 'search.views.index'),
     
     
)
