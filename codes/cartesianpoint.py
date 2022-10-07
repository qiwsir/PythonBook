#coding:utf-8
'''
filename: cartesianpoint.py
'''
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def __str__(self):
        return f"Point is ({self.x}, {self.y})"
    
    __repr__ = __str__

    def __setitem__(self, key, value):
        print("you are calling __setitem__() method.")
        self.__dict__[key] = value
        
    def __getitem__(self, item):
        print("you are calling __getitem__() method.")
        if item == "x":
            return f"{self.x}"
        elif item == 'y':
            return f"{self.y}"
        else:
            return "There is no this item."