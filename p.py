#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""

import os,time,random
from time import sleep

def gitpush(fn,commit='by q',delfn=True):
    os.system('git add '+fn)
    os.system('git commit -m "'+ commit +'"')
    os.system('git push origin master')
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
