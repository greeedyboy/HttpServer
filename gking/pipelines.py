# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import hashlib
from scrapy.conf import settings

class GkingPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        shart = settings["MONGODB_SHART"]
        shtoken=settings["MONGODB_SHTOKEN"]

        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.postart = mydb[shart]
        self.posttoken = mydb[shtoken]

    def process_item(self, item, spider):

        token=self.get_token(str(item['fromlink']))

        result = self.posttoken.find_one({'token': token})

        # print(result)
        # print('\n' * 20)

        if result is not None:
             pass
        else:
            item['token'] = token
            data = dict(item)
            self.postart.insert(data)
            self.posttoken.insert({'token': token})
        return item


    def get_token(self,md5str):
        # 生成一个md5对象
        m1 = hashlib.md5()
        #使用md5对象里的update方法md5转换
        m1.update(md5str.encode("utf-8"))
        token = m1.hexdigest()
        return token