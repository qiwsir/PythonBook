#coding:utf-8
'''
filename: moresugar.py
'''
def p_decorate(func):
    def wrapper(name):
        return f"<p>{func(name)}</p>"
    return wrapper

def div_decorate(func):
    def wrapper(name):
        return f"<div>{func(name)}</div>"
    return wrapper

@div_decorate
@p_decorate
def book(name):
    return f"the name of my book is {name}"

if __name__ == "__main__":
    result = book("PYTHON")
    print(result)