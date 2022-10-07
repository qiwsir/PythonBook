#coding:utf-8
"""
filename: multitable.py
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}x{i}={i*j}", end=" ")
    print()