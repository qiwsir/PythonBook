#coding:utf-8
'''
filename: choiceprime.py
'''
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def choice(*args):
    return [i for i in args if is_prime(i)]

if __name__ == "__main__":
    prime_number = choice(1,3,5,7,9,11,13,15,17,19,21,23)
    print(prime_number)