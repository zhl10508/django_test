# -*- coding: utf-8 -*-


import subprocess
import os,subprocess
#import airtest


serialno = None # if multi device, must specify serialno
appname = ''#'com.netease.itown.tdg.oppo'
#device = airtest.ANDROID

activity_map ={'com.netease.itown.tdg.netease':'com.netease.itown.tdg.netease.Launcher'}


#得到当前的安卓设备
def getDevices(device='android'):
    '''
    @return devices list
    '''
    subprocess.call(['adb', 'start-server'])
    output = subprocess.check_output(['adb', 'devices'])
    result = []
    for line in str(output).splitlines()[1:]:
        ss = line.strip().split()
        if len(ss) == 2:
            (devno, state) = ss
            result.append((devno, state))
    return result


################################################
########不用airtest############################
##################################################

#adb获取包名
def adb_package(app_info=''):
    p = subprocess.Popen('adb shell pm list packages -3',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    sout = p.stdout.readlines()
    sout = [i.replace("package:","").replace('\r','').replace('\n','') for i in sout]
    if app_info=='':
        return sout
    result = []
    for one in sout:
        if app_info in one:
            result.append(one)
    return result

#给定app，appname，卸载
def adb_uinstall(appname):
    print 'try to uninstall ',appname
    unistall_str = subprocess.call('adb shell pm uninstall '+appname)
   # app_path = "/sdcard/Android/data/" + appname
   # unistall_str1 = app.dev.adb.shell('rm -r '+app_path)
    # 内网的安装目录要手动删下
    app_path = "/sdcard/netease/itown.tdg_daily.common"
    unistall_str1 = subprocess.call('adb shell rm -r '+app_path)
    print unistall_str,unistall_str1

#给定apk 来安装
def adb_install(apk_path):
    print 'try to install app,',apk_path
    #subprocess.Popen(['adb', 'install',apk_path])
    subprocess.call(['adb', 'install',apk_path])
    import time
    # for i in xrange(20):
    #     print i,'install...'
    #     time.sleep(1)
    #app.click(u'安装.png')
    print 'end install'

#给定apk 来启动
def adb_start(app_name):
    print app_name
    subprocess.call(['adb', 'shell', 'am', 'start', '-n', '/'.join([app_name, activity_map[app_name]])])
    print 'start over'

#给定坐标 adb点击
def adb_touch(x,y):
    print 'adb touch ',x,y
    subprocess.call('adb shell input tap '+str(x)+' '+str(y))

#滑动
def adb_swipe(x1,y1,x2,y2):
    print 'adb swipe',x1,x2,y1,y2
    subprocess.call('adb shell input swipe '+str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2))

#发送系统消息具体请查阅 <android keycode详解> http://blog.csdn.net/huiguixian/article/details/8550170
def adb_keyevent(keyid):
    print 'adb input keyevent id ',keyid
    subprocess.call('adb shell input keyevent '+str(keyid))

#截图
def adb_snap(filename='sreen.png'):
    tmpname = '/sdcard/test.png'
    subprocess.call('adb shell screencap -p '+tmpname)
    subprocess.call('adb pull /sdcard/test.png ' +filename)

#得到手机的分辨率
def getRestrictedScreen():
    ''' Gets C{mRestrictedScreen} values from dumpsys. This is a method to obtain display dimensions '''
    print 'in getRestrictedScreen'
    p = subprocess.Popen('adb shell dumpsys window ', stdout=subprocess.PIPE)
    out_p =p.communicate()
    outlines = out_p[0]
    outlines= outlines.splitlines()
   # print outlines
    import re
    rsRE = re.compile('\s*mRestrictedScreen=\((?P<x>\d+),(?P<y>\d+)\) (?P<w>\d+)x(?P<h>\d+)')
    for line in outlines:
        m = rsRE.match(line)
        if m:
            return m.groups()
    # in order to competiable with android-2.3.5
    dsRE = re.compile('\s*DisplayWidth=(?P<x>\d+) DisplayHeight=(?P<y>\d+)')
    for line in outlines:
        m = dsRE.match(line)
        if m:
            return (0, 0) + m.groups()
    raise RuntimeError("Couldn't find mRestrictedScreen in dumpsys")

def adbmain(apk_path='now.apk'):
    pacs = adb_package('tdg')
    print pacs
    if pacs:
        #卸载掉对应的apk
        for oneapk in pacs:
            if 'netease' in oneapk:
                adb_uinstall(oneapk)
    adb_snap()
    adb_install(apk_path)
    adb_touch(365,775)
    adb_keyevent(4)
    adb_swipe(140,650,200,650)
    print 'start app'
    tdg_pac = adb_package('tdg')
    app_name = tdg_pac[0]
    adb_start(app_name)
    
if __name__ =="__main__":
    #print getDevices()
    apk_url = "http://192.168.10.116/binary/ios_ipa_publish/tdg_netease.apk"
    print 'start to download'
    #subprocess.call('wget -N '+apk_url+' -O now.apk -o wget.log')  # -O tdg_netease.apk
    #print 'end download'
   # adbmain()
    #print getRestrictedScreen()
    print getDevices()
    # import socket
    # HOSTNAME = 'localhost'
    # TIMEOUT = 15
    # try:
    #     PORT = int(os.environ['ANDROID_ADB_SERVER_PORT'])
    # except KeyError:
    #     PORT = 5037
    # tsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tsocket.settimeout(TIMEOUT)
    # tsocket.connect((HOSTNAME, PORT))
    # print tsocket
