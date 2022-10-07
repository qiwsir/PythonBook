#coding:utf-8
'''
filename: chromosome.py
'''
import random

class Father:
    def __init__(self):
        self.father_chromosome = 'XY'
    
    def do(self):
        print("Make money.")

class Mother:
    def __init__(self):
        self.mother_chromosome = "XX"
    
    def do(self):
        print("Manage money.")

class Child(Father, Mother):
    def child_gender(self):
        fat = random.choice(self.father_chromosome)
        mot = 'X'
        chi = fat + mot
        if "Y" in chi:
            return 1
        return 0

if __name__ == "__main__":
    p = Child()
    if p.child_gender():
        print('is a BOY.')
    else:
        print("is a GIRL.")