#coding:utf-8
'''
filename: mymodule.py
'''
class Book:
    __lang = "python"
    def __init__(self, author):
        self.__author = author
    
    def get_name(self):
        return (self.__author, self.__lang)

def foo(x):
    return x * 2

if __name__ == '__main__':
    python = Book("laoqi")
    python_name = python.get_name()
    x = 2
    mul_result = foo(x)