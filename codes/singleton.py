#coding:utf-8
'''
filename: singleton.py
'''
class Singleton:
    _instance = None  #⑪
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)   #⑫
        return cls._instance 

class MyBook(Singleton): 
    def __init__(self, name):
        self.name = name

 
if __name__ == "__main__":
    b1 = MyBook("learn python")
    b2 = MyBook("mathematics for ML")
    print(b1)
    print(b2)
    print("b1 is b2: ", b1 is b2)
    print(f"b1.name = {b1.name}")
    print(f"b2.name = {b2.name}")
    print("b1.name is b2.name:", b1.name is b2.name)