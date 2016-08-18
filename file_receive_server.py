# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:24:15 2016

@author: GUANGMING ZHAO
"""


import hprose

def save_file(name,data):
    f=open(name, "w")
    f.write(data)
    f.close() 

def save_img(name,data):
    f=open(name, "wb")
    f.write(data)
    f.close() 

def main():
    server = hprose.HttpServer(host="9.186.56.48",port = 5656)
    server.timeout=1000000
    server.addFunction(save_file)
    server.addFunction(save_img)
    server.start()
if __name__ == "__main__":
    main()