#coding:utf-8
"""
filename: multitable2.py
"""
for i in range(1, 10):
    j = 1
    while j <= i:
        print(f"{j}x{i}={i*j}", end=' ')
        j += 1
    print()