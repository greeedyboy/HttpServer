#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
from gking.plugin.creatart import git_post
from apscheduler.schedulers.blocking import BlockingScheduler

import subprocess

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=120)
def timed_job():
    print('This job is run every five minutes.')

    print('begin to scrapy crawl gking')
    # # bellow is ok
    rs=subprocess.check_output(['python','runspider.py','gking'])
    print(rs)

    print('begin to gking post')
    res=git_post()
    data={"postnum":str(res)}
    print(data)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()