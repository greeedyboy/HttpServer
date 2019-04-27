#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
import scrapy
from scrapy.crawler import CrawlerProcess
from gking.items import GkingItem
import json
from urllib import parse as pars
from scrapy import signals

from gking.plugin.aqgetsets import load_sets


class gkingspider(scrapy.Spider):

    name = "gking"

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(NankaiSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    #     return spider
    #
    #
    # def spider_closed(self, spider):
    #     spider.logger.info('Spider closedxxxxxx: %s', spider.name)
    #
    # def spider_stopped(self, spider):
    #     spider.logger.info('Spider stoppedxxxxxx: %s', spider.name)


    def start_requests(self):  # 由此方法通过下面链接爬取页面
        # 定义爬取的链接
        # print('loading................................')
        spset = load_sets()
        urldic=dict(spset['urls'])
        # urldic={'http://news.nankai.edu.cn/nkyw/index.shtml':'nankai',
        #         'http://news.nankai.edu.cn/qqxy/index.shtml':'nankai'}

        for url,val in urldic.items():

            yield scrapy.Request(url=url, callback=self.parse,meta={'methodkey':val},dont_filter=True)  # 爬取到的页面如何处理？提交给parse方法处理


    def parse(self, response):

        # spset = load_sets()

        newslist= self.parse_cont(['newslist'], response)['newslist']
        # 根据method来处理获取页面列表


        # 送入内容处理阶段
        for newslink in newslist:
            # print(newslink)
            # print("+++++++++++++++++++++++++++++++++++++++++++++")
            newslink = pars.urljoin(response.url, newslink)
            # print(newslink)
            # print(".....................................")
            yield scrapy.Request(newslink,callback=self.content,meta={'url': newslink,'methodkey':response.meta['methodkey']})


    def content(self,response):
        item=GkingItem()

        res = self.parse_cont(['title','content','imgs','tags','categories'], response)

        imgls=[]

        for newslink in res['imgs']:
            newslink = pars.urljoin(response.url, newslink)
            imgls.append(newslink)


        item['fromlink'] = response.url
        item['method'] = response.meta['methodkey']
        item['title']=res['title']
        item['content']=res['content']
        item['imgs']=imgls
        item['tags']=res['tags']
        item['categories']=res['categories']


        yield item

    # def load_sets(self):
    #     with open('spiderset.json', 'r', encoding='utf-8') as b_oj:
    #         settings = json.load(b_oj)
    #     ## print(settings)
    #     return settings


    def parse_cont(self,contlist,response):

        methodkey=response.meta['methodkey']

        if not isinstance(contlist, list):
            conts=[contlist]
        else:
            conts=contlist.copy()

        reslist=[]

        spset = load_sets()

        for cont in conts:
            method = spset['methods'][methodkey][cont]

            if cont=='tags':
                res=method
                reslist.append(res)
                continue
            if cont=='categories':
                res=method
                reslist.append(res)
                continue

            sel = method['sel']
            selstr = method['selstr']
            seltype = method['seltype']
            if sel=='css':
                if seltype=='extract':
                    res = response.css(selstr).extract()
                elif seltype=='extract_first':
                    res = response.css(selstr).extract_first()
                else:
                    res = response.css(selstr).extract()
            else:
                res = response.css(selstr).extract()
            pass
            reslist.append(res)

        resdict=dict(map(lambda x,y:[x,y],conts,reslist))

        return resdict


# process = CrawlerProcess()
# process.crawl(NankaiSpider)
# process.start()