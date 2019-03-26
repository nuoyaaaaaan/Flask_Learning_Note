#coding=utf-8
'''
Create on 19-3-23

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''

from flask import Flask

app = Flask(__name__)
app.debug = True


"""
1.decorator = app.route('/', methods=["GET", "POST"], endpoint='n1')
    def route(self, rule, **options):
        # self = app对象
        # rule = /
        # options = methods=["GET", "POST"], endpoint='n1'
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
2.@decorator 
    decorator(index)
"""


@app.route('/', methods=["GET", "POST"], endpoint='n1')
def index():
    return "hello world"


def login():
    return '登录'


app.add_url_rule('/login', 'n2', login, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run()
