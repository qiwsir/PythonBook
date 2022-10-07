#coding:utf-8
'''
filename: convertletter.py
'''
def convert(s):
    """
    convert upper and lower in a string.
    convert(string) -> string
    """
    lst = [e.upper() if e.islower() else e.lower() for e in s]
    return "".join(lst)

if __name__=="__main__":
    word = "Python"
    new_word = convert(word)
    print(f"{word} --> {new_word}")