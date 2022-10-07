# coding=utf-8
'''
filename: private.py
'''
class ProtectMe: 
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "laoqi"

    def __python(self):  
        print("I love Python.")

    def code(self):
        print("What language do you like?")
        self.__python()   

if __name__ == "__main__": 
    p = ProtectMe()
    p.code()
    print(p.me)
    p.__python()  