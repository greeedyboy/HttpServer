# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# """info
#
# """
# from scrapy import cmdline
#
# import traceback
# import os,sys
#
#
# def run_scrapy(name='gking'):
#     try:
#         sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#
#         dir_path = os.path.dirname(os.path.abspath(__file__))
#         # os.system('cd /d '+ dir_path)
#         # print(dir_path)
#         # os.system('scrapy crawl '+ name)
#
#         # execute(["scrapy", "crawl", name])  # 这样一行代码就可以了
#         # print(dir_path+'\sc.bat')
#         # os.system(r''+dir_path+'\sc.bat')
#
#         import subprocess
#
#         subprocess.check_output(['scrapy', 'crawl', name])
#         # subprocess.Popen("python scrapy crawl gking")
#         # cmdline.execute("scrapy crawl gking".split())
#
#         state=True
#     except:
#         traceback.print_exc()
#         state=False
#
#     return state
#
# # run_scrapy('gking')