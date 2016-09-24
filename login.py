#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import sys

'''author:lidage'''

reload(sys)

capurl = "http://202.207.247.44:8059/validateCodeAction.do"        #验证码地址
posturl = "http://202.207.247.44:8059/loginAction.do"              #登陆地址

# cookie自动管理

cookie = cookielib.CookieJar()
hand = urllib2.HTTPCookieProcessor(cookie)

# opener与cookie绑定

opener = urllib2.build_opener(hand)

# 用户登陆
username =raw_input('请输入你的学号：')
password =raw_input('请输入你的密码：')

# 用opener先访问验证码，得到验证码cookie由cookie管理器自动管理

picture = opener.open(capurl).read()
local = open('//home/lidage/PycharmProjects/course/image.jpg','wb') # 验证码写入本地proje目录下验证码
local.write(picture)                                                # 显示验证码
local.close()
code = raw_input('请输入验证码：')                                    # 人工识别验证码e

headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'35',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'202.207.247.44:8059',
        'Origin':'http://202.207.247.44:8059',
        'Referer':'http://202.207.247.44:8059/logout.do',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            }

postdatas= {
    'zjh':username,
    'mm':password,
    'v_yzm':code,
}

# 模拟登陆教务处
data = urllib.urlencode(postdatas)
request = urllib2.Request(posturl,data,headers)
try:
    response = opener.open(request)
    html = response.read().decode('gbk')
    print html
except urllib2.HTTPError,e:
    print e.code
