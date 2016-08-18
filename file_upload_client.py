# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:25:10 2016

@author: GUANGMING ZHAO
"""

import hprose
client = hprose.HttpClient('http://9.186.56.48:5656/')
client.timeout=1000000
   
import time
import datetime
import os
localtime_str=(datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y%m%d")


def upload_logs(from_logs_path,to_logs_path):
    files=os.listdir(from_logs_path)
    localtime_str=(datetime.date.today() + datetime.timedelta(days=0)).strftime("%Y%m%d")
    for file_name in files:
        if localtime_str in file_name:
            print(file_name)
            f=open(from_logs_path+"/"+file_name)
            ff=f.read()   #以read()方法取得文件全部内容。
            client.save_file(to_logs_path+"/"+file_name,ff)
            f.close()
    


def upload_imgs(from_img_path,to_img_path):
    files=os.listdir(from_img_path)
    localtime_str=(datetime.date.today() + datetime.timedelta(days=0)).strftime("%Y%m%d")
    for file_name in files:
        if localtime_str in file_name:
            print(file_name)
            f=open(from_img_path+"/"+file_name,'rb')
            ff=f.read()   #以read()方法取得文件全部内容。
            client.save_img(to_img_path+"/"+file_name,ff)
            f.close()
    


if __name__ == '__main__':
#    upload_logs("logs","logs")
#    upload_imgs("img","img")
    while True:
        #每天1点上传上一天日志和图片到指定server
        if(int(time.strftime("%H", time.localtime()))==1):
            upload_logs("logs","logs")
            upload_imgs("img","img")
        time.sleep(60*60)