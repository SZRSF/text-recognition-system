class Config:
    DEBUG = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zxcvbnm123456@47.98.181.132:3306/Ocr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
