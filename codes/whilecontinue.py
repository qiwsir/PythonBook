#coding:utf-8
'''
whilecontinue.py
'''
a = 11
while a > 0:
    a -= 1
    if a % 2 == 0:
        continue  # (3)
        print(a)  # (4)
    else:
        print(a)  # (5)