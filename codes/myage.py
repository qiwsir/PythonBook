#coding:utf-8
"""
filename: myage.py
"""
# age = input('please input your age:')  # (1)
# age = int(age)                         # (2)
# if age < 60:                           # (3)
#     print('你还没退休')                  # (4)
#     delta = 60 - age
#     print(f'再过{delta}年就退休了')       # (5)
# centenarian = 100 - age                 # (6)
# print(f'距离人瑞尚有{centenarian}年')

# age = input('please input your age:')  
# age = int(age)                         
# if age < 60:                           
#     if age < 18:                       # (7)
#         print("good good study")
#     if age >= 18 and age < 50:         # (8)
#         print("work hard")
#     print('你还没退休')                
#     delta = 60 - age
#     print(f'再过{delta}年就退休了')    
# centenarian = 100 - age                
# print(f'距离人瑞尚有{centenarian}年')

age = input('please input your age:') 
if age.isnumeric():
    age = int(age)
    if age < 7:
        print('还没上学呢')
    elif age >=7 and age < 25:
        print('莫等闲，白了少年头，空悲切')
    elif age >= 25 and age < 35:
        print('关关雎鸠，在河之洲')
    elif age >=35 and age < 60:
        print('会当凌绝顶')
    else:
        print('廉颇老矣，尚能饭否')
else:
    print("请输入数字")