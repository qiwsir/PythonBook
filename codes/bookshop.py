#coding:utf-8
'''
filename: bookshop.py
'''

class Book:
    prices = {"A":45.7, "B":56.7, "C":67.8, "D":78.9, "E":90.1}
    shipping = 5    # 快递费单价：5元/本
    
    def __init__(self, book_name, num, free_ship):
        self.book_name = book_name
        self.num = num
        self.free_ship = free_ship    # 免快递费的阈值

    # 计算总价
    def totals(self):
        price = Book.prices.get(self.book_name) 
        if price:
            t = price * self.num
            return (t + Book.shipping) if t < self.free_ship else t
        return "There is NO this book."

if __name__ == "__main__":
    book_a = Book('A', 2, 100)
    a_total = book_a.totals()
    print(a_total)