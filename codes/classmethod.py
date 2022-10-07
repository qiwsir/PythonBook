#coding:utf-8
'''
filename: clssmethod.py
'''
class Message:
    msg = "Python is a smart language."  
    def get_msg(self):
        print("the self is:", self)  
        print("attrs of class(Message.msg):", Message.msg)

    @classmethod  
    def get_cls_msg(cls):
        print("the cls is:", cls) 
        print("attrs of class(cls.msg):", cls.msg)

if __name__ == "__main__": 
    mess = Message()
    mess.get_msg()
    print("-" * 20)
    mess.get_cls_msg()