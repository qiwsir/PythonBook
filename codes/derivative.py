#coding:utf-8
'''
filename: derivative.py
'''
class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h      
        return (f(x+h) - f(x))/h