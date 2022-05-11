from datetime import datetime

from ext import db


class User(db.Model):   # 表名将会是user
    """
    id:表的id，自增
    username:用户名，非空
    password:密码:非空
    email:邮箱，非空
    radtetime:注册时间
    dev:当前登录的设备信息
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64),nullable=False)
    radtetime = db.Column(db.DateTime, default=datetime.now())
    dev = db.Column(db.String(100))

    def __str__(self):
        return self.username


class Picture(db.Model):    # 表名 picture 存储文字识别过程中相关信息
    """
    id:自增id
    picUrl：图片存放路径
    OCR_txt:图片转成文本存储
    author_id:外键，与user表主键关联
    """
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    picUrl = db.Column(db.String(100),nullable=False)
    OCR_txt = db.Column(db.String(1000))
    author_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))