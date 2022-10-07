#coding:utf-8
'''
filename: newmethod.py
'''
class Human:
    def __new__(cls, *args, **kwargs):
        # cls = Human. cls is the class using which the object will be created.
        # Created object will be of type cls.
        # We must call the object class' __new__ to allocate memory
        obj = super().__new__(cls) # This is equivalent to object.__new__(cls)

        print(type(obj)) # Prints: <__main__.Human object at 0x103665668>
        print(id(obj))
        # return the object
        return obj
    
    def __init__(self, first_name, last_name):
        print("Inside __init__ method")
        # self = human_obj returned from the __new__ method

        self.first_name = first_name
        self.last_name = last_name
        print(f"{self}")
        print(id(self))