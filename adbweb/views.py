# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import adb,os
import settings

#处理url里的creat
def index(request):
    print 'in Chane'
    #return HttpResponse('test index')
    data = {}
    data['text'] = 'test dffds df'
    try:
        img_path =  os.path.join(settings.STATIC_ROOT,'img')
        file_name = os.path.join(img_path,'temp.png')
        print 'file_name:',file_name
        adb.adb_snap(filename=file_name)
    except:
        print 'error in adb snap'
    img_url = '/static/img/temp.png'
    data['img'] = img_url
    return render_to_response('adb.html',data)

def ajax_getxy(request):
    print 'in ajax_getxy'
    #print request.GET
    adb_type = int(request.GET['type'])
    x1 =  int(request.GET['x1'])
    y1 =  int(request.GET['y1'])
    x2 =  int(request.GET['x2'])
    y2 =  int(request.GET['y2'])
    x = (x1+x2)/2
    y = (y1+y2)/2
    #左起点
    click_point=(x,y)
    swipe_points = (x1,y,x2,y)
    if adb_type==1:
        print 'click point ',click_point
        try:
            import adb 
            adb.adb_touch(x,y)
            #print dir(adb)
        except:
            HttpResponse('error in click point'+str(click_point))
    elif adb_type==2:
        import adb
        swipe_points = (x1,y,x2,y)
        adb.adb_swipe(x1,y,x2,y)
        print 'swipe' ,swipe_points
    elif adb_type==3:
        swipe_points = (x2,y,x1,y)
        import adb 
        adb.adb_swipe(x2,y,x1,y)
        print 'swipe' ,swipe_points
    return HttpResponse('OK')