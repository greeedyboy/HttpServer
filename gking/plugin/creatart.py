#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
import pymongo
import os,json,time,random
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
    name = settings['MONGODB_USER']
    password = settings['MONGODB_PASSWORD']

    # 创建MONGODB数据库链接
    # 'mongodb://root:123456@localhost:27017/'
    client = pymongo.MongoClient(host=host, port=port)
    # 指定数据库
    mydb = client[dbname]
    mydb.authenticate(name=name, password=password)

    #数据库文章表
    postart = mydb[shart]
    results = postart.find()
    # content=""
    # result=results[0]
    res='that is all'
    num=0

    #open backdb存在备份json则打开
    work_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(work_dir)
    bakjson='dbbak.json'
    dbdic={}
    if os._exists(bakjson):
        with open(bakjson, 'r', encoding='utf-8') as b_oj:
            dbdic = json.load(b_oj)
    # print(work_dir)

    #加载设置
    sets = load_sets()['posts']
    token='xxxxxxxxxxxx'
    for result in results:
        dbs=result
        [token,strs]=dbs_art(dbs)

        # print(strs)
        print('article token:'+token)
        print('*' * 50)
        # 写入临时文件
        fn='tempfile.md'
        with open(fn, 'w',encoding='utf-8') as f:
            f.write(strs)

        #加载设置后进行api更新操作
        apis=sets[dbs['method']]
        ghtest=GhOper(fromfx=fn,tofx=token+'.md',apis=apis)

        res=ghtest.gh_api_ops()

        if res[0]:#成功则删除数据数据
            num=num+1
            #成功后存入bakjson
            dbdic[token]=strs

            result = postart.delete_many({'token': token})
            pass
    print('post news number is ' + str(num))

    if num>0:
        # 将dict写入文件，然后提交数据库
        with open(bakjson, 'w', encoding='utf-8') as b_oj:
            json.dump(dbdic, b_oj,indent=4, ensure_ascii=False)

        # 获得当前时间时间戳
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeStruct = time.localtime(now)
        dats = time.strftime("%Y%m%d%H%M%S", timeStruct)

        tofx='db'+dats+'_'+token+'.json'

        ghtest = GhOper(fromfx=bakjson, tofx=tofx, apis=['api_bak'])
        res = ghtest.gh_api_ops()

        if res[0]:
            os.remove(bakjson)
            print('success upload file '+ tofx )

    return num
        # print(res)