#coding:utf-8
'''
filename: nestfor.py
'''
num = []
i = 2
for i in range(2, 30):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)

print(num)