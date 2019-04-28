#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""info

"""
import base64

s1='40ab6290da9a5c2ddd43760511a01e8af21b5187'
encodestr = base64.b64encode(s1.encode('utf-8'))
ss=str(encodestr,'utf-8')
print(ss)

token='zdYWJjcjM0cjM0NHI='


token=str(base64.b64decode(token[2:].encode('utf-8')),'utf-8')
print(token)