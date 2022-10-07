#coding:utf-8
'''
filename: metaclass.py
'''
class AuthorMeta(type):
    def __new__(cls, name, bases, attrs):
        print("AuthorMeta is called.")
        attrs['__author__'] = "laoqi" 
        return type.__new__(cls, name, bases, attrs)

class Python(metaclass=AuthorMeta):
    def __init__(self, bookname):
        self.bookname = bookname
        
    def author(self):
        return self.__author__