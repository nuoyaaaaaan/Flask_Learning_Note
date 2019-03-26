#coding=utf-8
'''
Create on 19-3-23

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from flask import Flask, views


app = Flask(import_name=__name__)
#  这里需要同步在hosts文件中添加网址和ip的对应关系不然无法正常运行
"""
127.0.0.1  hezongxing.com
127.0.0.1  admin.hezongxing.com
127.0.0.1  buy.hezongxing.com
"""
app.config['SERVER_NAME'] = 'hezongxing.com:5000'

@app.route('/', subdomain='admin')
def static_index():
    return "xxxxxx.your-domain.tld"

@app.route('/dynamic', subdomain="<username>")
def username_index(username):
    return username + ".your-domian.tld"


if __name__ == '__main__':
    app.run()