#coding=utf-8
'''
Create on 19-3-23

@auther: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from flask import Flask, views


app = Flask(__name__)
app.debug = True
app.secret_key = 'safsd2'

@app.route('/index', methods=["GET", "POST"], endpoint='n1', strict_slashes=False, redirect_to="/index2")
def index():
    return "公司老首页"

@app.route('/index2', methods=["GET", "POST"], endpoint='n2', strict_slashes=False)
def index2():
    return "公司新首页"


if __name__ == '__main__':
    app.run()