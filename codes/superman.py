#coding:utf-8
"""
filename: superman.py
"""

class SuperMan:                # (1)
    '''                        # (2)
    A class of superman
    '''
    def __init__(self, name):  # (3)
        self.name = name       # (4)
        self.gender = 1        # (5)
        self.single = False    
        self.illness = False
    def nine_negative_kungfu(self):  # (6)
        return "Ya! You have to die."

zhangsan = SuperMan("zhangsan")  # (7)
print("superman's name is:", zhangsan.name)   # (8)
print("superman is:(0-female, 1-male) ",zhangsan.gender)  # (9)

result = zhangsan.nine_negative_kungfu()  # (10)
print("If superman play nine negative kungfu, the result is:")
print(result)
