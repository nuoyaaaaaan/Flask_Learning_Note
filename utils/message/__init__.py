#coding=utf-8
'''
Create on 19-3-25

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
import importlib

import settings

def send_msgs(msg):

    for path in settings.MSG_LIST:
        m, c = path.rsplit('.', maxsplit=1)
        md = importlib.import_module(m)
        obj = getattr(md, c)()
        obj.send(msg)


