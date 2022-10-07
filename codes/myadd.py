#coding:utf-8
"""
filename: myadd.py
"""
def add(x, y):
    '''
    This is an addition function.
    add(3, 4) -> 7.0
    '''
    r = x + y
    return float(r)

if __name__ == "__main__":
    sum = add(2, 4)
    print(sum)