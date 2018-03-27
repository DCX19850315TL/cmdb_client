#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2018/3/21 17:32
'''
import httplib
import urllib
import time
import json

def RequestUrl(host,port,source,params,timeout):
    headers = {"Content-type":"application/json"}
    try:
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        original = response.read()
        print original
    except Exception,e:
        raise e
    return original

server_info={
    'hwaddr':'00:00:0c:12:23:34'
    'cpu':'x86_64'
}

if __name__ == '__main__':
    #times = 0
    #while True:
        RequestData = {'data':server_info}
        RequestData = json.dumps(RequestData)
        result = RequestUrl('127.0.0.1','9000','/receive_server_info/',RequestData,30)
        print '======第%d次请求，结果为: %s========= %(times,result)'
        #times += 1
        #time.sleep(3)