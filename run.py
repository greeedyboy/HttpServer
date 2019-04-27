# -*- coding: utf-8 -*-

# @Date    : 2018-10-26
# @Author  : Peng Shiyu
import sys
sys.path.append("..")
from gking.plugin.creatart import git_post
# from runscrapy import run_scrapy
import os
import subprocess
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gkingcrawl")
def gkingcrawl():

    print('begin to scrapy crawl gking')
    # # bellow is ok
    rs=subprocess.check_output(['python','runspider.py','gking'])
    return "ok"
    pass

@app.route("/gkingpost")
def gkingpost():
    res=git_post()
    data={"postnum":str(res)}
    return jsonify(data)
    pass

@app.route("/get")
def get():
    headers = dict(request.headers)
    data = {}
    data["headers"] = headers
    data["url"] = request.url
    data["args"] = request.args
    data["remote_addr"] = request.remote_addr

    return jsonify(data)


@app.route("/post", methods=["POST"])
def post():
    headers = dict(request.headers)
    data = {}
    data["headers"] = headers
    data["url"] = request.url
    data["form"] = request.form
    data["remote_addr"] = request.remote_addr

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
