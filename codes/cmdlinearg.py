#coding:utf-8
'''
filename: cmdlinearg.py
'''
import sys

x = sys.argv[1]
y = sys.argv[2]
print(f"{x} + {y} = {float(x) + float(y)}")
print(f'sys.argv = {sys.argv}')
print(f'the file is {sys.argv[0]}')