#coding:utf-8
'''
filename: agebirth.py
'''
import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def by_birth(cls, name, birth_year):
        this_year = datetime.date.today().year
        age = this_year - birth_year
        return cls(name, age)  #⑥
    def get_info(self):
        return "{0}'s age is {1}".format(self.name, str(self.age))

if __name__ == "__main__":
    newton = Person('Newton', 26)  #⑦
    print(newton.get_info())
    hertz = Person.by_birth("Hertz", 1857)  #⑧
    print(hertz.get_info())