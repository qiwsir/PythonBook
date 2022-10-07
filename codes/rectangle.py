#coding:utf-8
'''
filename: rectangle.py
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# class Square:
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length

#     def perimeter(self):
#         return 4 * self.length

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# class RightPyramid(Square, Triangle):
#     def __init__(self, base, slant_height):
#         self.base = base
#         self.slant_height = slant_height
#         super().__init__(self.base)
#         self.height = slant_height

#     def area(self):
#         base_area = super().area()
#         #perimeter = super().perimeter()
#         tri_area = Triangle.area(self)
#         #return 0.5 * perimeter * self.slant_height + base_area
#         return tri_area * 4 + base_area

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        Square.__init__(self, self.base)
        Triangle.__init__(self, self.base, self.slant_height)

    def area(self):
        base_area = super(Square, self).area()
        #perimeter = super().perimeter()
        tri_area = Triangle.area(self)
        #return 0.5 * perimeter * self.slant_height + base_area
        return tri_area * 4 + base_area

if __name__ == "__main__":
    # cube = Cube(2)
    # print(cube.surface_area())
    # print(cube.volume())
    pyramid = RightPyramid(2, 4)
    print(pyramid.area())