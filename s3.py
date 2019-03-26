#coding=utf-8
'''
Create on 19-3-23

@auther: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''

from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = "afsdf1erq"
# app.config['debug'] = True
# app.config.from_pyfile('settings.py')
# app.config.from_object("python类或类的路径")
app.config.from_object("settings.DevelopmentConfig")



@app.route('/', methods=["GET"])
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()