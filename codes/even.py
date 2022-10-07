#coding:utf-8
'''
filename: even.py
'''
import random

lst = []
for i in range(20):
    lst.append(random.randint(1, 10))

print(lst)

# for n in lst:
for idx, n in enumerate(lst):
    if n % 2 == 0:
#        idx = lst.index(n)
        lst[idx] = 'even'

print(lst) 