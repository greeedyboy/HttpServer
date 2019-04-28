#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""info

"""
from gking.plugin.creatart import git_post
res = git_post()
data = {"postnum": str(res)}

print(data)