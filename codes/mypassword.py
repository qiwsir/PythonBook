#coding:utf-8
'''
filename: mypassword.py
'''
class User:
    def __init__(self):
        self.__password = 'default'
    
    @property
    def password(self):
        return self.__password

    @password.setter                 
    def password(self, value):
        value = int(value) + 728     # 最低级的加密方法
        self.__password = str(value)
        print("you have set your password.")