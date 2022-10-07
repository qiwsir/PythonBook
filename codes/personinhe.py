#coding:utf-8
'''
filename: personinhe.py
'''
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self, school, name, age):    # 增加参数
        self.school = school
        super().__init__(name, age)
        # super(Student, self).__init__(name, age)
        # Person.__init__(self, name, age)

    def grade(self, n):
        print(f"{self.name}'s grade is {n}")

 
if __name__ == "__main__":
    # stu1 = Student("Galileo", 27)
    stu1 = Student("Social University", "Galileo", 27)
    stu1.grade(99) 
    print(stu1.get_name()) 
    print(stu1.get_age()) 
    print(stu1.school)              # 增加一行