#coding=utf-8
'''
Create on 19-3-23

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from flask import Flask, views


app = Flask(__name__)
app.debug = True


def auth(func):
    def inner(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result
    return inner


class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [auth, ]

    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index.POST'


app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name = endpoint


if __name__ == '__main__':
    app.run()
