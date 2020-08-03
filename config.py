import os
import random
import string


class Config(object):
    CSRF_ENABLE = True
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nicdom3115@localhost:5432/app_flask_estoque'


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = '8001'
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'  # ip do servidor na nuvem (geralmente)
    PORT_HOST = '5000'
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'  # Ip do servidor de produção
    PORT_HOST = '8080'
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig(),
}

app_active = os.getenv('FLASK_ENV')
