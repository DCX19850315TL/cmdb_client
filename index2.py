#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index2.py.py
@time: 2018/3/27 17:14
'''
import httplib
import urllib
import json

try:
    test = '{"data":1111}'
    JsonData = json.dumps(test)

    httpClient = httplib.HTTPConnection('127.0.0.1','9000','10')
    httpClient.request('POST','/receive_server_info/',JsonData)
    response = httpClient.getresponse()
    orgint = response.read()
    print orgint
except Exception,e:
    print e