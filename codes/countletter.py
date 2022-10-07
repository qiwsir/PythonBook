#coding:utf-8
'''
filename: countchar.py
'''
word = input('please input an english word:')
result = {}
for e in word:
    if e in result:
        result[e] += 1
    else:
        result[e] = 1
print(f'the word is: {word}')
print(f'count letter: {result}')