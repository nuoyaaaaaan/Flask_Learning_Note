#coding=utf-8
'''
Create on 19-3-23

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''

DEBUG = True


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

