#coding:utf-8
'''
filename: fibsgenerator.py
'''
def fibs():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

if __name__ == "__main__": 
    import itertools
    print(list(itertools.islice(fibs(), 10)))