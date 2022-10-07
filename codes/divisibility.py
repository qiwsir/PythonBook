#coding:utf-8
"""
filename: divisibility.py
"""
# lst = []
# for i in range(50):
#     if i % 3 == 0:
#         lst.append(i)

lst = [i for i in range(50) if i % 3 == 0]
print(f"numbers divisible by 3: {lst}")
