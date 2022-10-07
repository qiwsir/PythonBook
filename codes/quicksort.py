#coding:utf-8
'''
filename: quicksort.py
'''
import statistics

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median([
            numbers[0], 
            numbers[len(numbers)//2], 
            numbers[-1]])
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot])
        return (
            quick_sort(items_less) + \
                pivot_items + \
                    quick_sort(items_greater))

import random

def get_random_numbers(length, minimum=1, maximum=100):
    return [random.randint(minimum, maximum) for _ in range(length)]

if __name__=='__main__':
    nums = get_random_numbers(10, -50, 50)
    print(nums)
    nums_sorted = quick_sort(nums)
    print(nums_sorted)