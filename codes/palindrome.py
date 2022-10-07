#coding:utf-8
'''
filename: palindrome.py
'''

def contains_palindrome(words):
    for word in words:
        if word == ''.join(reversed(word)):
            return True
    return False

def contains_palindrome_s(words):
    return any(word == ''.join(reversed(word)) for word in words)

if __name__ == '__main__':
    lst = ['why', 'your', 'eye', 'is', 'large']
    print(contains_palindrome_s(lst))