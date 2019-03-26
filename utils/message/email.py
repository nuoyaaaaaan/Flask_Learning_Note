#coding=utf-8
'''
Create on 19-3-25

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from .base import Base


class Email(Base):
    """
    发送邮件相关数据提醒
    """
    def __init__(self):
        """
        邮箱相关数据初始化
        """
        self.username = 'asdf'
        self.pwd = 'asdf'

    def send(self, msg):
        pass

