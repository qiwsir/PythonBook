#coding:utf-8
'''
filename: debugprint.py
'''
import pdb
def mean(x, y):
    print(f"{x}==>{type(x)}")
    print(f"{y}==>{type(y)}")
    # pdb.set_trace()            # 到此则自动暂停
    return x + y / 2

if __name__ == "__main__":
    a = input('input an integer：')
    b = input('input an other integer: ')
    aver = mean(a, b)
    print(f"{aver} is the average of {a} and {b}")