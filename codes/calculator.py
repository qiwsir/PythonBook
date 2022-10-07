#coding:utf-8
'''
calculator.py
'''
class Calculator:
    is_raise = True
    def calc(self, expression):
        try:
            # if '4' in expression:
            #     raise Exception("4 should not be in the expression.")
            assert ('4' not in expression), "assert: 4 should not be in the expression."
            return eval(expression)
        except ZeroDivisionError:
            print("零不能做分母，小学生都知道。")
            raise
        except NameError as e:
            print(e)
            return "表达式不正确。"
        except Exception as e4:
            return e4

if __name__ == "__main__":
    cal = Calculator()
    result = cal.calc("4 / 2")
    print(result)