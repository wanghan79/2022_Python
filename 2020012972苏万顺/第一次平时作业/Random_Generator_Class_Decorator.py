"""
Author: WanshunSu 2020012972
Purpose: First python class homework in spring semester, 2022
Introduction:
           A class for generate some random numbers or strings,It is implemented using decorator.
           It and 'test.py' are a whole.
           If you want to test this class, Please run 'test.py','test3' in the 'test.py' file tests this function.
Created: 2022/5/29
"""
import random
from functools import wraps

class Random_Generator_Class_Decorator(object):
    '''
    This class is a decorated class
    '''
    def __init__(self,**kwargs):
        '''

        :param **kwargs:parameters passed in.
        '''
        self.kwargs = kwargs

    def __call__(self, func, *args, **kwargs):
        '''
        Rewrite this function to make it a decorative class
        And then use @wraps() to keep function's own namespace
        '''
        @wraps(func)
        def wrapper(**kwargs):
            data = self.generate(**(self.kwargs))
            return func(data, **kwargs)
        return wrapper

    def Input_checks(self):
        '''
        Check whether the input data is legal.
        '''
        if self.kwargs['num'] <= 0:
            raise Exception("num should be greater than 0, but now it is less than or equal to 0")
        for index in range(0, self.kwargs['num']):
            for key, value in self.kwargs['struct'].items():
                if key == "int":
                    if isinstance(value['datarange'], tuple) == False:
                        raise Exception("datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                    if len(value['datarange']) != 2:
                        raise Exception("datarange should have 2 numbers")
                    if value['datarange'][1] - value['datarange'][0] < self.kwargs['num']:
                        raise Exception("The range of random numbers you want to generate is smaller than the number of random numbers you want to generate")
                    if value['datarange'][1] - value['datarange'][0] <= 0:
                        raise Exception("The second number in your datarange is less than the first number")
                elif key == "float":
                    if isinstance(value['datarange'], tuple) == False:
                        raise Exception("datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                    if len(value['datarange']) != 2:
                        raise Exception("datarange should have 2 numbers,but now it has {} numbers".format(type(value['datarange'])))
                    if value['datarange'][1] - value['datarange'][0] <= 0:
                        raise Exception("The second number in your datarange is less than the first number")
                elif key == "str":
                    if isinstance(value['datarange'], str) == False:
                        raise Exception("datarange should be a str,but now it is {}".format(type(value['datarange'])))
                    if value['strlen'] <= 0:
                        raise Exception("strlen should be greater than 0, but now it is less than or equal to 0")

    def generate(self,**kwargs):
        '''
        Functions that generate random numbers.
        '''
        self.Input_checks()
        result = list()
        try:
            for index in range(0, kwargs['num']):
                element = []
                for key, value in kwargs['struct'].items():
                    if key == "int":
                        it = iter(value['datarange'])
                        tmp = random.randint(next(it), next(it))
                    elif key == "float":
                        it = iter(value['datarange'])
                        tmp = random.uniform(next(it), next(it))
                    elif key == "str":
                        tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
                    else:
                        break
                    element.append(tmp)
                result.append(element)
            return result
        except TypeError:
            print("The Type is error.")
        except MemoryError:
            print("The Memory is error.")
        except ValueError:
            print("The value is not correct")
        except Exception as e:
            print(e)
            print("ERROR")
        finally:
            print("The generated data is:")