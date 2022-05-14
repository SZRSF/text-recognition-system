from flask import Flask

from apps.user import user_bp
from ext import db
from setting import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)  # 加载配置
    # 初始化db
    db.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    return app
