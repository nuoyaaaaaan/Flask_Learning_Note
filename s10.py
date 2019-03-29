#coding=utf-8
'''
Create on 19-3-25

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from flask import Flask, render_template, Markup
app = Flask(__name__)
app.debug = True


def func1(arg):
    return Markup("<input type='text' value='%s' />" % (arg,))

@app.route('/')
def index():
    return render_template('s10index.html', ff=func1)


if __name__ == '__main__':
    app.run()

