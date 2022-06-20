"""
Author: WanshunSu 2020012972
Purpose: Third python class homework in spring semester, 2022
Introduction:
           A function for generate some random numbers or strings and calculate ACC and MCC,It is implemented using decorator.
           It and 'test.py' are a whole.
           If you want to test this function, Please run 'test.py','test1' in the 'test.py' file tests this function.
Created:2022/6/3
"""
import random
import string
import math
from functools import wraps

def struct(static="ACC"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result:
                if (e[0] is True) and (e[1] is True):
                    TP += 1
                elif (e[0] is True) and (e[1] is False):
                    FN += 1
                elif (e[0] is False) and (e[1] is True):
                    FP += 1
                elif (e[0] is False) and (e[1] is False):
                    TN += 1
                else:
                    pass
            if static == "ACC":
                ACC = (TP + TN) / total
                print("ACC : %f" % ACC)
            elif static == "MCC":
                MCC = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % MCC)
            else:
                pass
            return result
        return wrapper
    return decorator

@struct("MCC")
@struct("ACC")
def structDataSampling(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    try:
        result = list()
        for index in range(0, kwargs['num']):
            element = list()
            for key, value in kwargs['struct'].items():
                if key == "int":
                    if isinstance(value['datarange'], tuple) == False:
                        raise Exception("datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                    if len(value['datarange']) != 2:
                        raise Exception("datarange should have 2 numbers")
                    if value['datarange'][1] - value['datarange'][0] < kwargs['num']:
                        raise Exception("The range of random numbers you want to generate is smaller than the number of random numbers you want to generate")
                    if value['datarange'][1] - value['datarange'][0] <= 0:
                        raise Exception("The second number in your datarange is less than the first number")
                    else:
                        it = iter(value['datarange'])
                        element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    if isinstance(value['datarange'], tuple) == False:
                        raise Exception("datarange should be a tuple,but now it is {}".format(type(value['datarange'])))
                    elif len(value['datarange']) != 2:
                        raise Exception("datarange should have 2 numbers,but now it has {} numbers".format(type(value['datarange'])))
                    elif value['datarange'][1] - value['datarange'][0] <= 0:
                        raise Exception("The second number in your datarange is less than the first number")
                    else:
                        it = iter(value['datarange'])
                        element.append(random.uniform(next(it), next(it)))
                elif key == "str":
                    if isinstance(value['datarange'], str) == False:
                        raise Exception("datarange should be a str,but now it is {}".format(type(value['datarange'])))
                    elif value['strlen'] <= 0:
                        raise Exception("strlen should be greater than 0, but now it is less than or equal to 0")
                    else:
                        element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen'])))
                elif key == "bool":
                    if isinstance(value['datarange'], int) == False:
                        raise Exception("data should be int,but now it is {}".format(type(value['datarange'])))
                    if value['datarange'] <= 0:
                        raise Exception("data should be greater than 0, but now it is less than or equal to 0")
                    else:
                        for i in range(value['datarange']):
                            element.append(random.choice((True, False)))
                else:
                    break
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
        pass
        '''
        If you want to output the random bool data of production, you can uncomment the following code
        '''
        # print("The generated data is:")
        # for item in result:
        #     print(item)
        # print('############################')