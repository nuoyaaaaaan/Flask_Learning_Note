#coding=utf-8
'''
Create on 19-3-25

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from flask import Flask, session
app = Flask(__name__)
app.debug = True
app.secret_key = '260168'
app.session_interface


@app.route('/')
def index():
    # flask内置的使用， 加密cookie（签名cookie）来保存数据
    session['k1'] = 'v1'
    session['k2'] = 'v2'

    pass


if __name__ == '__main__':
    app.run()

