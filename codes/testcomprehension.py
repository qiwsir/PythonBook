#coding:utf-8
'''
filename:testcomprehension.py
'''
import time

start = time.time()
lst = [i * i for i in range(100000)]
end = time.time()
delta = end - start

print(f"list comprehension time: {delta}")

start2 = time.time()
lst2 = []
for i in range(100000):
    lst.append(i * i)
end2 = time.time()
delta2 = end2 - start2

print(f"for loop time: {delta2}")
print(f"(list comprehension) / (for loop) = {delta/delta2:.3f}")