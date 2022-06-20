"""
Author: WanshunSu 2020012972
Purpose: Final python class homework in spring semester, 2022
Introduction:
            A class for generate some random numbers or strings,It is implemented using iterator.
            It and 'ACC_MCC_Decorator.py' and 'test.py' are a whole,The purpose is
            to calculate ACC and MCC of randomly generated groups of Boolean data.
            If you want to test this class and 'ACC_MCC_Decorator.py', Please run 'test.py',
            'Random_Generator' in the 'test.py' file tests this class and 'ACC_MCC_Decorator.py'.
Created:2022/6/3
"""
import random
from .ACC_MCC_Decorator import ACC_MCC_Decorator

class Random_Generator_Class_Iterator(object):
    '''
    This class is a Iterator class
    '''
    def __init__(self,**kwargs):
        '''
        :param **kwargs:parameters passed in.
        '''
        self.kwargs = kwargs
        self.num = self.kwargs['num']
        self.struct = self.kwargs['struct']

    def Input_checks(self):
        '''
        Check whether the input data is legal.
        '''
        if self.num <= 0:
            raise Exception("num should be greater than 0, but now it is less than or equal to 0")
        for index in range(0, self.num):
            for key, value in self.struct.items():
                if key == "int":
                    if isinstance(value['datarange'], tuple) == False:
                        raise Exception("datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                    if len(value['datarange']) != 2:
                        raise Exception("datarange should have 2 numbers")
                    if value['datarange'][1] - value['datarange'][0] < self.num:
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
                elif key == "bool":
                    if isinstance(value['datarange'], int) == False:
                        raise Exception("data should be int,but now it is {}".format(type(value['datarange'])))
                    if value['datarange'] <= 0:
                        raise Exception("data should be greater than 0, but now it is less than or equal to 0")

    def __iter__(self,**kwargs):
        '''
        Functions that generate random numbers,Generate using yield.
        '''
        self.Input_checks()
        try:
            # print("The generated data is:")
            for index in range(self.num):
                if index == self.num:
                    raise StopIteration
                element = []
                for key, value in self.struct.items():
                    if key == "int":
                        it = iter(value['datarange'])
                        element.append(random.randint(next(it), next(it)))
                    elif key == "float":
                        it = iter(value['datarange'])
                        element.append(random.uniform(next(it), next(it)))
                    elif key == "str":
                        element.append(
                            ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen'])))
                    elif key == "bool":
                        for i in range(value['datarange']):
                            element.append(random.choice((True, False)))
                    else:
                        break
                yield element
                '''
                If you want to output the random bool data of production, you can uncomment the following code
                '''
                # print(element)
        except TypeError:
            print("The Type is error.")
        except MemoryError:
            print("The Memory is error.")
        except ValueError:
            print("The value is not correct.")
        except Exception as e:
            print(e)
            print("ERROR")
        finally:
            print('############################')
            print("ACC and MCC are respectively:")

@ACC_MCC_Decorator("MCC")
@ACC_MCC_Decorator("ACC")
def Random_Generator(**kwargs):
    randoms = Random_Generator_Class_Iterator(**kwargs)
    result = []
    for element in randoms:
        result.append(element)
    return result