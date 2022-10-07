#coding:utf-8
'''
filename: mydict.py
'''
class IntFloatValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} is invalid input, CustomIntFloatDict can only accept integers and floats as its values'

class KeyValueContructError(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return 'keys and values need to be passed as either list or tuple' + '\n' + \
                f' {self.key} is of type: {str(type(self.key))}' + '\n' + \
                f' {self.value} is of type: {str(type(self.value))}'


class CustomIntFloatDict(dict):
    empty_dict = {}
    
    def __init__(self, key=None, value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key, (tuple, list,)) or not isinstance(value, (tuple, list)):
            raise KeyValueContructError(key, value)
        else:
            zipped = zip(key, value)
            for k, val in zipped:
                if not isinstance(val, (int, float)):
                    raise IntFloatValueError(val)
                dict.__setitem__(self, k, val)

    def get_dict(self):
        return self.empty_dict

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise IntFloatValueError(value)
        return dict.__setitem__(self, key, value)

# #testing

# test_1 = CustomIntFloatDict()
# print(test_1)
test_2 = CustomIntFloatDict({'a', 'b'}, [1, 2])
print(test_2)
# # test_3 = CustomIntFloatDict(('x', 'y', 'z'), (10, 'twenty', 30))
# # print(test_3)
# test_4 = CustomIntFloatDict(('x', 'y', 'z'), (10, 20, 30))
# print(test_4)
# test_4['r'] = 1.3
# print(test_4)
# test_4['key'] = 'bad_value'