# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import settings

#处理url里的creat
def index(request):
    data = {}
    return render_to_response('zl_base.html',data)

