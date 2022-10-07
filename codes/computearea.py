#coding:utf-8
'''
filename: computearea.py
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    rect = Rectangle(7, 8)
    #rect_area = rect.area()
    print(f"width = {rect.width}, height = {rect.height}")
    print(f"call rect.area attribute to rectangle area = {rect.area}")