#coding:utf-8
'''
filename: catspeak.py
'''
class Cat:
    ears = 2
    legs = 4
    def __init__(self, color):
        self.color = color

    @staticmethod
    def speak():
        print("Meow, Meow")

if __name__ == "__main__":
    black_cat = Cat("black")
    white_cat = Cat("white")
    black_cat.speak()
    white_cat.speak()
    if black_cat.speak is white_cat.speak and black_cat.speak is Cat.speak:
        print('black_cat.speak, white_cat.speak, Cat.speak are the same objects.')