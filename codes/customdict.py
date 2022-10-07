#coding:utf-8
'''
filename: customdict.py
'''
class Simdict:
    def __init__(self, k, v):
        self.__dct = dict([(k, v),])
    
    def __setitem__(self, k, v):
        self.__dct[k] = v
    
    def __getitem__(self, k):
        return self.__dct[k]
    
    def __delitem__(self, k):
        del self.__dct[k]
    
    def __str__(self):
        return f"{self.__dct}"

    __repr__ = __str__

    def __len__(self):
        return len(self.__dct)
    
if __name__ == "__main__":   
    d = Simdict('name', 'Laoqi')
    print(d)
    d['lang'] = 'python'
    d['city'] = 'Soochow'
    print(d['city'])
    print(len(d))
    print(d)
    del d['city']
    print(d)

