#coding:utf-8
'''
filename: editattr.py
'''
class Book:
    def __init__(self, name):
        self.name = name
        self.book = "mathematics for ML by laoqi"
    def __getattr__(self, attr):
        print("you should learn from Laoqi.")
    def __setattr__(self, attr, value):
        # super().__setattr__(attr, value)
        if attr == 'author':                # (2)
            super().__setattr__(attr, 'Laoqi')
        else:
            super().__setattr__(attr, value)

    def __delattr__(self, attr):
        if attr == 'book':
            raise AttributeError("你必须看老齐的这本书.")
        else:
            super().__delattr__(attr)