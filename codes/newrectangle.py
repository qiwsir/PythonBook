#coding:utf-8
'''
filename: newrectangle.py
'''

class NewRectangle:
    def __init__(self):
        self.width = 0
        self.length = 0
        
    def __getattr__(self, name):
        if name == "size": 
            return self.width, self.length
        else:
            raise AttributeError
    
    def __setattr__(self, name, value):
        if name == "size": 
            self.width, self.length = value
        else:
            super().__setattr__(name, value)

if __name__ == "__main__":
    rect = NewRectangle()
    rect.width = 3
    rect.length = 4
    print(f"rect.size: {rect.size}")
    rect.size = 30, 40
    print(f"with: {rect.width}")  
    print(f"length: {rect.length}")