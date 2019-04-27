#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
import pymongo
from scrapy.conf import settings
# import scrapy.settings
from gking.plugin.aqtp2art import dbs_art
from gking.plugin.gitsender import GhOper
from gking.plugin.aqgetsets import load_sets

def git_post():
    host = settings["MONGODB_HOST"]
    port = settings["MONGODB_PORT"]
    dbname = settings["MONGODB_DBNAME"]
    shart = settings["MONGODB_SHART"]
    shtoken = settings["MONGODB_SHTOKEN"]

    # 创建MONGODB数据库链接
    client = pymongo.MongoClient(host=host,port=port)
    # 指定数据库
    mydb = client[dbname]
    postart = mydb[shart]


    results = postart.find()
    # content=""
    # result=results[0]
    res='that is all'
    num=0
    for result in results:
        dbs=result
        [token,strs]=dbs_art(dbs)
        print(strs)
        print('*' * 50)

        fn='tempfile.md'
        with open(fn, 'w',encoding='utf-8') as f:
            f.write(strs)

        # settingfile='././spiderset.json'
        sets=load_sets()['posts']
        apis=sets[dbs['method']]

        ghtest=GhOper(fromfx=fn,tofx=token+'.md',apis=apis)

        res=ghtest.gh_api_ops()

        if res[0]:#成功则删除数据数据
            num=num+1
            result = postart.delete_many({'token': token})
            pass
    print('post news number is ' + str(num))
    return num
        # print(res)