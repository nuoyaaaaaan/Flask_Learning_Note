#coding=utf-8
'''
Create on 19-3-26

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
from flask import Flask, request
from utils import msg
from utils.message import send_msgs


app = Flask(__name__)
app.debug = True


@app.route('/warn1', methods=["GET"])
def index_warn1():

    data = request.query_string.get('val')
    if data == 'hzx':
        #  发送报警：短信/邮件
        msg.email('warning')
        msg.message('warning')

    return "hello world warn1"


@app.route('/warn2', methods=['GET'])
def index_warn2():
    data = request.query_string.get('val')
    if data == 'hzx':
        send_msgs('......')
        pass

    return 'hello world warn2'


if __name__ == '__main__':
    app.run()

