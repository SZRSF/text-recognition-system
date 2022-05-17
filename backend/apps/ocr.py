import base64
import io
import json
import os
import random
import string
import time
import urllib.parse
import urllib.request

import numpy as np
from PIL import Image
from flask import Blueprint, request, json

ocr_bp = Blueprint('ocr', __name__)

# 定义一个目录用于保存图片
basedir = os.path.abspath(os.path.dirname(__file__))

def posturl(url,data={}):
    # 请求头
    headers = {
        'Authorization': 'APPCODE 19acfca7e95d4492a63aa1a1b7ed3d59',  # APPCODE +你的appcod,一定要有空格！！！
        'Content-Type': 'application/json; charset=UTF-8'  # 根据接口的格式来
    }
    try:
        params=json.dumps(data).encode(encoding='UTF8')
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html =r.read()
        r.close()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    time.sleep(1)


@ocr_bp.route('/api/general_ocr', methods=['POST'])
def general_ocr():
    # 获取前端传过来的base64图片格式
    upload_image = request.form['image']
    # 获取前端传过来的文件名
    filename = request.form['filename']
    # 将base64图片格式转码
    img = Image.open(io.BytesIO(base64.b64decode(upload_image)))
    # 定义一个图片存放的位置 存放在static下面
    path = basedir + "../../images/"
    # 图片path和名称组成图片的保存路径
    file_path = path + filename
    # 保存图片
    img.save( file_path)
    # 图片url
    url = './images/'+filename
    print(url)
    # 以二进制读取本地图片
    with open(url, 'rb') as f:
        data = f.read()
        # base64编码图片
        encodestr = str(base64.b64encode(data), 'utf-8')
    # 对照官网API改
    url_request = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"
    dict = {'img': str(encodestr)}
    html = posturl(url_request, data=dict)

    # <class 'str'>
    print(html, type(html))
    # str转json对象，<class 'dict'>
    jos = json.loads(html)
    print(jos, type(jos))
    # 就可以按key取值了
    result = jos['content']
    print('识别的结果：', result)
    return json.dumps(result),200