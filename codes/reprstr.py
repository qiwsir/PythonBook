#coding:utf-8
'''
filename: reprstr.py
'''
class Book:
    def __init__(self, author, book_name):
        self.author = author
        self.book_name = book_name

    def __str__(self):
        return self.book_name

    def __repr__(self):
        return f"{self.book_name} by {self.author}"

if __name__ == "__main__":
    py = Book('laoqi', 'PYTHON')
    print(py)
    print([py])