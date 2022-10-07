#coding:utf-8
'''
filename: customlist.py
'''
class Mylist(list):         # 继承 list
    def __getitem__(self, index):
        if index == 0:
            raise IndexError
        if index > 0:
            index = index - 1
            return list.__getitem__(self, index) # this method is called when
                                                 # we access a value with subscript like x[1]
    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError
        if index > 0:
            index = index - 1
            list.__setitem__(self, index, value)

if __name__ == "__main__":
    lst = Mylist(['python', 'java', 'julia'])   # __init__() inherited from builtin list
    print(lst)                                  # __repr__() inherited from builtin list
    lst.append('PHP');                          # append() inherited from builtin list
    print(f"lst[1] is {lst[1]}")                # 'python' (Mylist.__getitem__ cutomizes list superclass
                                                # method. index is 1, but reflects 0!
    print (f"lst[4] is {lst[4]}")               # 'PHP' (index is 4 but reflects 3!
    lst[2] = 'R'
    print(lst)