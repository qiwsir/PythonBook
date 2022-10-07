#coding:utf-8
'''
filename: sumhundred.py
'''
sum = 0
# for i in range(1, 101):
#     sum += i
result = [sum := sum + i for i in range(1, 101)]
print(f"the sum of 1 to 100 is: {result[-1]}")