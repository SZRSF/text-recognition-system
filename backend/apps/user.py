from flask import Blueprint, request, jsonify, render_template

from apps.model import User
from ext import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return render_template('index.html')


# 注册
@user_bp.route('/api/register', methods=['POST'])
def register():
    # 获取post提交的数据
    my_json = request.get_json()
    print(my_json)
    username = my_json.get("username")
    password = my_json.get("password")
    email = my_json.get("email")
    flag = 1
    # 1.找到模型并创建对象
    user = User()
    # 判断是否有存在要注册的账户
    users = user.query.all()
    for u in users:
        if u.username == username:
            flag = 0
    if flag == 1:
        # 2.给对象的属性赋值
        user.username = username
        user.password = password
        user.email = email
        # 添加
        # 3.将user对象添加到session中（类似缓存)
        db.session.add(user)
        # 4.提交数据库
        db.session.commit()
        res = {
            "code": 201,
            "data": {
                "id": user.id,
                "name": user.username,
                "email": user.email,
                "tags": "注册成功"
            }
        }
        return jsonify(res)
    else:
        res = {
            "code": 501,
            "data": {
                "id": "",
                "name": "",
                "email": "",
                "tags": "注册失败，用户名重复"
            }
        }
        return jsonify(res)


@user_bp.route('/api/login', methods=['get', 'POST'])
def login():
    # 获取post提交的数据
    my_json = request.get_json()
    print(my_json)
    username = my_json.get("username")
    password = my_json.get("password")
    # 关键 select * from user where username = 'xxxx'
    # 查询
    user_list = User.query.filter_by(username=username)
    print(user_list)
    for u in user_list:
        # 此时的 U 表示的就是用户对象
        if u.password == password:
            res = {
                "code": 201,
                "data": {
                    "id": u.id,
                    "name": u.username,
                    "password": u.password,
                    "email": u.email,
                    "tags": "登录成功"
                }
            }
            return jsonify(res)
        else:
            res = {
                "code": 501,
                "data": {
                    "id": "",
                    "name": "",
                    "password": "",
                    "email": "",
                    "tags": "登录失败，密码错误"
                }
            }
            return jsonify(res)
    return jsonify({
        "code": 502,
        "data": {
            "id": "",
            "name": "",
            "password": "",
            "email": "",
            "tags": "登录失败，用户不存在"
        }})
