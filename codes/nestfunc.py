#coding:utf-8
'''
filename: nestfunc.py
'''

def power_generator(num):
    def power_n(power):
        return num ** power
    return power_n

if __name__ == "__main__":
    power_two = power_generator(2)
    power_three = power_generator(3)
    print(power_two(8))
    print(power_three(2))