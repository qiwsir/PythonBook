#coding:utf-8
'''
filename: decorate.py
'''

def p_decorate(func):
    def wrapper(name):
        #return "<p>{0}</p>".format(func(name))
        return f"<p>{func(name)}</p>"
    return wrapper

@p_decorate   
def book(name):
    #return "the name of my book is {0}".format(name)
    return f"the name of my book is {name}"


if __name__ == "__main__":
    # my_book = p_decorate(book)
    # result = my_book("PYTHON")
    result = book("Learn Python")
    print(result)