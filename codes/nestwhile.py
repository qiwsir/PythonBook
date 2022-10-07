#coding:utf-8
'''
filename: nestwhile.py
'''
num = []
i = 2
while (i < 30):
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j += 1
    if (j > i / j):
        num.append(i)
    i += 1

print(num)
