#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""

import os,time,random
from time import sleep
from boto.s3.connection import S3Connection

def gitpush(fn,commit='by q',delfn=True):
    os.system('git init')
    os.system('git config --global user.email "greedyboy@163.com"')
    os.system('git config --global user.name "greedyboy"')
    os.system('git add '+fn)
    os.system('git commit -m "'+ commit +'"')
    #from boto.s3.connection import S3Connection
    #s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
    #git push --force --quiet "https://greedyboy:${CO_TOKEN}@${CO_REF}" master:master
    #token=S3Connection(os.environ['token'])
    token='937285aa64c3043d9281d9f2a5c9eee255fdc835'
    comdstr='git push --force --quiet "https://greedyboy:'+ token +'@github.com/greedyboy/HttpServer.git"'
    os.system(comdstr)
    
    if delfn:
        os.remove(fn)


def creat_file(strx=''):
    randx=random.randint(1000, 9999)
    fn= 'blog/'+ time.strftime("%Y%m%d%H%M%S", time.localtime())+str(randx)+'.txt'
    with open(fn, 'a+') as f:
        f.write(fn + '\n')  # 加\n换行显示
        f.write(strx)
    return fn


def runx():
  strlist=['how','are','you']
  for strx in strlist:
      fn=creat_file(strx=strx)
      print('pushing ' + fn)
      gitpush(fn=fn,commit=strx)
