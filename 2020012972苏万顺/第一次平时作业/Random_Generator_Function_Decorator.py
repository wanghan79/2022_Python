"""
Author:WanshunSu
Purpose:
Introduction:
           A function for generate some random numbers or strings,It is implemented using decorator.
           It 'test.py' are a whole.
           If you want to test this function, Please run 'test.py','test2' in the 'test.py' file tests this function.
Created:2022/5/29
"""
import random
from functools import wraps
# import string
def Random_Generator_Function_Decorator(func):
    '''
    This function is a decorated function
    '''
    def decorator(func):
        '''
        use @wraps() to keep function's own namespace
        '''
        @wraps(func)
        def wrapper(**kwargs):
            try:
                result = list()
                for index in range(0, kwargs['num']):
                    element = list()
                    for key, value in kwargs['struct'].items():
                        if key == "int":
                            if isinstance(value['datarange'], tuple) == False:
                                raise Exception(
                                    "datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                            if len(value['datarange']) != 2:
                                raise Exception("datarange should have 2 numbers")
                            if value['datarange'][1] - value['datarange'][0] < kwargs['num']:
                                raise Exception("The range of random numbers you want to generate is smaller than the number of random numbers you want to generate")
                            if value['datarange'][1] - value['datarange'][0] <= 0:
                                raise Exception("The second number in your datarange is less than the first number")
                            else:
                                it = iter(value['datarange'])
                                tmp = random.randint(next(it), next(it))
                        elif key == "float":
                            if isinstance(value['datarange'], tuple) == False:
                                raise Exception("datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                            elif len(value['datarange']) != 2:
                                raise Exception("datarange should have 2 numbers,but now it has {} numbers".format(
                                    type(value['datarange'])))
                            elif value['datarange'][1] - value['datarange'][0] <= 0:
                                raise Exception("The second number in your datarange is less than the first number")
                            else:
                                it = iter(value['datarange'])
                                tmp = random.uniform(next(it), next(it))
                        elif key == "str":
                            if isinstance(value['datarange'], str) == False:
                                raise Exception(
                                    "datarange should be a str,but now it is {}".format(type(value['datarange'])))
                            elif value['strlen'] <= 0:
                                raise Exception(
                                    "strlen should be greater than 0, but now it is less than or equal to 0")
                            else:
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
                for item in result:
                    print(item)
                return func(**kwargs)
        return wrapper
    return decorator
