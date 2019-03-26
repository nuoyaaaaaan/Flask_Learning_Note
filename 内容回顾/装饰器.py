#coding=utf-8
'''
Create on 19-3-22

@author: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''
import datetime

def wrapper(func):
    def inner(*args, **kwargs):
        b_time = datetime.datetime.now()
        func(args[0])
        e_time = datetime.datetime.now()
        total_time = e_time - b_time
        print(total_time)
    return inner

@wrapper
def fbis(num):
    result = [0,1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    print(result)
    return result

if __name__ == '__main__':
    fbis(100)


