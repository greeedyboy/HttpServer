#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""


import sys
from scrapy import cmdline
# subprocess.Popen("scrapy crawl bking")
if len(sys.argv)>1:
    name=str(sys.argv[1])
    comds="scrapy crawl "+name
else:
    comds="scrapy crawl gking"

rs=cmdline.execute(comds.split())
