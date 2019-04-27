#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
# import pymongo
# from scrapy.conf import settings
import base64,json,requests
import random,time,sys,os


class GhOper():
    def __init__(self,apis,fromfx='',tofx='',msg='',settingfile='spiderset.json'):
        '''

        :param fn: 需要上传或更新的文件名。插入时候为本地文件名称 ，并且为远端名称。更新时候为本地文件包涵路径。
        :param apis: 使用的api
        :param message: 附带的commite信息
        :param settingfile: 设置文件
        '''
        dir_path = os.path.dirname(os.path.abspath(__file__))
        # print('当前目录绝对路径:', dir_path)
        # settingfile = dir_path + '\spiderset.json'

        self.fromfx=fromfx
        self.tofx=tofx
        self.msg=msg
        self.settingfile=dir_path + '/' + settingfile
        self.apis=apis
        pass

    def gh_api_ops(self):
        isoks=[]
        for api in self.apis:
            isok=self.gh_api_op(api=api)
            isoks.append(isok)

        return isoks

    def gh_api_op(self,api):
        # tokens='c2b9e3f5bf8dc58cc3ab4842b10fe08773e9788f'#greedyboy
        # tokens = 'c544055b75f6fb3b649522c6b987297b89c4f8e0'  # greeedyboy
        setss=self.load_set()


        sets=setss['apis'][api]

        gittoken=setss['gittokens'][sets['gittoken']]

        baseurl=sets['baseurl']
        dowhat=sets['dowhat']

        if self.msg:
            message = self.msg
        else:
            message = sets['message']

        name=gittoken['name']
        email=gittoken['email']
        tokens=gittoken['tokens']
        method=sets['method']
        typ=sets['typ']
        fromfx=sets['fromfx']

        # 目标路径表示
        tofx=sets['tofx']

        # 处理fromfx，tofx地址


        if self.fromfx:  # 函数引用不为空
            fromfx = self.fromfx

        if self.tofx:  # 函数引用不为空
            tofx = self.tofx

        # 新建或更新，来源于本地文件为file
        # fromfx输入为空则使用配置，不为空则为设定地址.
        # tofx输入为空则使用配置，配置为空则与fromfx相同
        # tofx 前缀含有http则使用tofx,不含有则将tofx加入到baseurl后面。

        if not tofx.startswith("https://"):  # 非网络地址
            tofx = baseurl + str(tofx)

        if typ=="url":
            if not fromfx.startswith("https://"):  # 非网络地址
                fromfx = baseurl + str(fromfx)




        headers = {"Authorization": 'token ' + tokens}  # 前两行会在后面的代码中忽略掉不写

        methodlist=['newfile','updatefile']
        xbase64 = ''
        if dowhat in methodlist:
            if typ=="file":
                xbase64=self.fn_base64(fromfx)
            elif typ=="url":
                r = requests.get(url=fromfx, headers=headers)
                if r.status_code == 200:
                    xbase64 = json.loads(r.text)['content']
            elif typ=='base64':
                xbase64=fromfx
            else:
                pass
        #
        # 新建文件
        if dowhat=='newfile':
            d = {"message": message,"committer": {"name": name,"email": email},"content": xbase64}
        # 新增评论
        elif dowhat=='newcomment':
            d = {"body": message}
            tofx=tofx+'/comments'
        # 更新文件,从本地更新
        elif dowhat=='updatefile':
            # 获取sha值
            r = requests.get(url=tofx, headers=headers)
            if r.status_code == 200:
                sha = json.loads(r.text)['sha']
            else:
                sha = ''
            # 获取
            d = {"message": message,"committer": {"name": name,"email": email},"content": xbase64,"sha":sha}
        # 更新文件，从git更新，默认
        else:
            d = {"message": message,"committer": {"name": name,"email": email},"content": xbase64}

        isok = False

        #put方法
        if method=='put':
            r = requests.put(url=tofx, data=json.dumps(d), headers=headers)
            if r.status_code==201 or r.status_code==200:
                isok = True
        if method=='post':
            r = requests.post(url=tofx, data=json.dumps(d), headers=headers)
            if r.status_code==201:
                isok = True
        if method=='get':
            r = requests.get(url=tofx, data=json.dumps(d), headers=headers)
            if r.status_code==200:
                isok=True
        else:
            pass

        return isok

    def update_file(self):
        pass

    def fn_base64(self,fn):
        # 打开本地图片，并转化为base64
        f = open(fn, 'rb')
        fnb64 = base64.b64encode(f.read()).decode('utf-8')
        return fnb64

    def load_set(self):
        with open(self.settingfile, 'r', encoding='utf-8') as b_oj:
            settings = json.load(b_oj)
        # print(settings)
        return settings


def creat_file(strx=''):
    randx=random.randint(1000, 9999)
    fn= ''+ time.strftime("%Y%m%d%H%M%S", time.localtime())+str(randx)+'.txt'
    with open(fn, 'a+') as f:
        f.write(fn + '\n')  # 加\n换行显示
        f.write(strx)
    return fn

# fromfx=creat_file('that')
#
# ghtest=GhOper(fromfx='hello-world.md',tofx='201904262009136948.txt',apis=['api_upu'],settingfile='E:/PycharmProjects/pyscrapy/gking/spiderset.json')
#
# res=ghtest.gh_api_ops()
#
# print(res)
#
# ghtest=GhOper(fromfx='1',apis=['api_c'],settingfile='E:/PycharmProjects/pyscrapy/gking/spiderset.json')
# res=ghtest.gh_api_ops()
# print(res)
#
# ghtest=GhOper(fromfx=creat_file('i am genxin'),apis=['api4'],settingfile='E:/PycharmProjects/pyscrapy/gking/spiderset.json')
# res=ghtest.gh_api_ops()
# print(res)