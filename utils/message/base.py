#coding=utf-8
'''
Create on 19-3-25

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''


class Base(object):

    def send(self, msg):
        raise NotImplementedError('...')
