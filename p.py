#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""

import os,time,random
from time import sleep
from boto.s3.connection import S3Connection

"""
- git clone https://${CO_REF} .deploy_git  # GH_REF是最下面配置的仓库地址
- cd .deploy_git
- git checkout master
- cd ../
- mv .deploy_git/.git/ ./public/   # 这一步之前的操作是为了保留master分支的提交记录，不然每次git init的话只有1条commit
- cd ./public
- git config user.name "greedyboy"  #修改name
- git config user.email "greedyboy@163.com"  #修改email
- git add .
- git commit -m "Travis CI Auto Builder at `date +"%Y-%m-%d %H:%M"`"  # 提交记录包含时间 跟上面更改时区配合
- git push --force --quiet "https://greedyboy:${CO_TOKEN}@${CO_REF}" master:master  #GH_TOKEN是在Travis中配置token的名称
:param fn: 
:param commit: 
:param delfn: 
:return: 
"""
def gitpush(fn,commit='by q',delfn=True):
    coref='github.com/greedyboy/HttpServer.git'
    # os.system('cd .deploy_git')
    # os.system('rm -rf .git')
    # os.system('cd ../')
    print('entre the cfn')
    os.system('cd cfn')
    print('git config user name')
    os.system('git config user.email "greedyboy@163.com"')
    os.system('git config user.name "greedyboy"')
    
    print('回到主目录')
    os.system('cd ../')
    print('clone git')
    os.system('git clone https://'+ coref +' cfn')

    print('checkout master')

    os.system('git checkout master')
    print('回到主目录')
    os.system('cd ../')
    print('移动 主目录blog文件到后面')
    os.system('mv ./'+ fn + ' ./cfn/'+fn)


    print('git add commit')
    os.system('git add '+fn)
    os.system('git commit -m "'+ commit +'"')


    # os.system('git init')
    # os.system('git config --global user.email "greedyboy@163.com"')
    # os.system('git config --global user.name "greedyboy"')
    # os.system('git add '+fn)
    # os.system('git commit -m "'+ commit +'"')
    #from boto.s3.connection import S3Connection
    #s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
    #git push --force --quiet "https://greedyboy:${CO_TOKEN}@${CO_REF}" master:master
    #token=S3Connection(os.environ['token'])
    token='937285aa64c3043d9281d9f2a5c9eee255fdc835'
    print('git push')
    comdstr='git push --force --quiet "https://greedyboy:'+ token +'@github.com/greedyboy/HttpServer.git" master:master'
    #comdstr='git push --set-upstream https://greedyboy:'+ token +'@github.com/greedyboy/HttpServer.git master'
    
    os.system(comdstr)

    
    # if delfn:
    #     os.remove(fn)


def creat_file(strx=''):
    randx=random.randint(1000, 9999)
    fn= 'blog/'+ time.strftime("%Y%m%d%H%M%S", time.localtime())+str(randx)+'.txt'
    with open(fn, 'a+') as f:
        f.write(fn + '\n')  # 加\n换行显示
        f.write(strx)
    return fn


def runx():
  strlist=['yyyyyy']

  for strx in strlist:
      fn=creat_file(strx=strx)
      print('pushing ' + fn)
      gitpush(fn=fn,commit=strx)

