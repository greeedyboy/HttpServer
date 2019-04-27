# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class GkingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    fromlink = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    categories = scrapy.Field()
    token=scrapy.Field()
    imgs=scrapy.Field()
    method=scrapy.Field()

    pass
