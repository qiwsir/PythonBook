#coding:utf-8
'''
filename: foo.py
'''
print(f"foo __name__ is set to {__name__}")

def main():
    print('The main() function was executed.')

if __name__ == '__main__':
    main()
else:
    print('Do not execute main() funciton!')