#coding:utf-8
'''
filename: fibonacci.py
'''

def fibo_loop(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

def fibo_recur(n):
    if n <= 1:
        return n
    else:
        return (fibo_recur(n-1) + fibo_recur(n-2))


if __name__ == "__main__":
    fib_lst = [fibo_recur(i) for i in range(10)]
    print(fib_lst)