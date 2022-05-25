from flask import Flask

from apps.listen import listen_bp
from apps.ocr import ocr_bp
from apps.user import user_bp
from ext import db
from setting import DevelopmentConfig


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # app是一个核心对象
    app.config.from_object(DevelopmentConfig)  # 加载配置
    # 初始化db
    db.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(ocr_bp)
    app.register_blueprint(listen_bp)
    return app
