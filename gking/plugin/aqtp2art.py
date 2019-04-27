#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
from gking.plugin.aqhtml2md import html_md
import time,os

dir_path = os.path.dirname(os.path.abspath(__file__))+'/'
# print('当前目录绝对路径:', dir_path)
# settingfile = dir_path + '\spiderset.json'

def str_replist(oldlist,newlist,tpfn='posttp.md'):



    with open(dir_path+tpfn,'r',encoding='utf-8') as f_obj:
        artstr = f_obj.read()

    dic = dict(map(lambda x, y: [x, y], oldlist, newlist))
    for k,v in dic.items():
        artstr=artstr.replace('$'+k+'$',v)

    return artstr

def dbs_art(dbs:dict,tpfn='posttp.md'):
    title=dbs['title']

    fromlink=dbs['fromlink']

    content = html_md(dbs['content'])

    simgs=''
    imgs = dbs['imgs']
    for img in imgs:
        if simgs:
            simgs='![图]('+ img +')'+'\n\n'+simgs
        else:
            simgs = '![图](' + img + ')'

    stags=''
    tags=dbs['tags']
    for tag in tags:
        if stags:
            stags='- '+tag+'\n'+stags
        else:
            stags = '- ' + tag

    scat=''
    categories=dbs['categories']
    for cat in categories:
        if scat:
            scat = '- ' + cat+ '\n' + scat
        else:
            scat = '- ' + cat

    token=dbs['token']
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    dats = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)

    oldlist=['title','date','urlname','tags','categories','content','imgs','fromlink']
    newlist=[title,dats,token,stags,scat,content,simgs,fromlink]

    strs=str_replist(oldlist,newlist,tpfn)

    for i in range(1,5):
        strs=strs.replace('\n\n\n','\n\n')

    return [token,strs]