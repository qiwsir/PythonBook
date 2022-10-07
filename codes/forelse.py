#coding:utf-8
'''
filename: forelse.py
'''
nums = [60, 70, 30, 110, 90]
# found = False
# for n in nums:
#     if n > 100:
#         found = True
#         print("There is a number bigger than 100")
#         break

# if not found:
#     print("Not found!")

for n in nums:
    if n > 100:
        print("There is a number bigger than 100")
        break
else:
    print("Not found!")

