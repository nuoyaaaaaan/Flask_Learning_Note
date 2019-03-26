
#coding=utf-8
'''
Create on 19-3-22

@auther: 260168

@requirements: PyCharm 2017.2.4, Python 3.6
'''


class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super(MyDict, self).__init__(*args, **kwargs)
        self['modify'] = True

    # def __setitem__(self, key, value):
    #     pass

obj = MyDict()
print(obj)
