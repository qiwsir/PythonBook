#coding:utf-8
'''
guessnumber.py
'''

import random
number = random.randint(1,100)
guess = 0
while True: 
    num_input = input("please input one integer that is in 1~100:") 
    guess += 1
    if not num_input.isdigit():
        print("Please input interger.") 
    elif int(num_input) < 0 or int(num_input) >= 100:
        print("The number should be in 1 to 100.") 
    else:
        if number == int(num_input): 
            print(f"OK, you’ve done well.It is only {guess} times.") 
            break
        elif number > int(num_input): 
            print("your number is smaller.") 
        else: 
            print("your number is bigger.") 