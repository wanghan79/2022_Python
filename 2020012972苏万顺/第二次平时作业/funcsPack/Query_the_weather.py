"""
Author:WanshunSu 2020012972
Purpose: Second python class homework in spring semester, 2022
Introduction:
           This is the class for querying weather,you can pass the 'test.py' to call it
Created:2022/5/30
"""
import requests
from collections.abc import Iterable, Iterator

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.__cities = cities

    def __iter__(self):
        return WeatherIterator(self.__cities)

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.__cities = cities
        self.__index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def __next__(self):
        if self.__index == len(self.__cities):
            raise StopIteration
        city = self.__cities[self.__index]
        self.__index += 1
        return self.getWeather(city)