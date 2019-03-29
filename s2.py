#coding=utf-8
'''
Create on 19-3-22

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''

from flask import Flask, render_template, request, redirect, session, url_for
import functools

#  实例化Flask对象
app = Flask(__name__)
app.debug = True

# @app.route('/')
# def index():
#     return 'hello world'


def user_auth(fun):
    @functools.wraps(fun)  # 保证装饰器不改变原函数的名称
    def inner(*args, **kwargs):
        user = session.get('user_info')
        if not user:
            # url = url_for('l1')
            return redirect('/login')
        else:
            return fun(*args, **kwargs)
    return inner


USER = {
    1: {'name': '贺宗星', 'age': 18, 'gender': '男', 'text': '111111111111'},
    2: {'name': '张黎', 'age': 18, 'gender': '女', 'text': '2222222222222'},
    3: {'name': '张秀蕊', 'age': 18, 'gender': '女', 'text': '33333333333'}
}


@app.route('/index', methods=['GET'])
@user_auth
def index():
    # user = session.get('user_info')
    # if not user:
    #     url = url_for('l1')
    #     return redirect(url)
        # return redirect('/login')
    return render_template('index.html', user_dict=USER)


@app.route('/detail/<int:nid>', methods=['GET'])
@user_auth
def detail(nid):
    # user = session.get('user_info')
    # if not user:
    #     return redirect('/login')
    info = USER.get(nid)
    return render_template('detail.html', info=info)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # request.query_string
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            return redirect('http://www.luffycity.com')
        return render_template('login.html', error='用户名或密码错误！')


if __name__ == '__main__':
    app.run()
