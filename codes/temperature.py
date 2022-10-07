#coding:utf-8
'''
temperature.py
'''
class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = value

    @temperature.deleter
    def temperature(self):
        raise AttributeError("Can't delete attribute")