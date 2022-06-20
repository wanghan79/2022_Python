"""
Author: WanshunSu 2020012972
Purpose: Second python class homework in spring semester, 2022
Introduction:
           This is the internal implementation of the function described in the 'test.py'
           This is some functions,you can pass the 'test.py' to call them
Created:2022/4/30
"""
from math import sqrt
from sys import stdout
import random
import string
def get_option():
    print("1:Read function body content through file")
    print("2:Calculate BMI")
    print("3:Read file")
    print("4:Generate random number")
    print("5:Generate prime number")
    print("6:Query the weather")
    print("7:exit")
    option = input("Please enter the action to be performed according to the prompt(numbers 1-7):")
    return option

def CalculateBMI(height,weight):
    '''

    :param height: height required to calculate BMI
    :param weight: weight required to calculate BMI
    :return:BMI value and constitution type
    '''
    bmi = weight / pow(height, 2)
    nat, dom = "", ""
    if bmi < 18.5:
        nat, dom = "thin", "thin"
    elif 18.5 <= bmi < 24:
        nat, dom = "normal", "normal"
    elif 24 <= bmi < 25:
        nat, dom = "normal", "overweight"
    elif 25 <= bmi < 28:
        nat, dom = "overweight", "overweight"
    elif 28 <= bmi < 30:
        nat, dom = "overweight", "obesity"
    else:
        nat, dom = "obesity", "obesity"
    return bmi, nat, dom

def txtFileReader(file):
    with open(file, encoding="utf-8") as f:
        count = 0
        for line in f.readlines():
            count += 1
            print('############################')
            print("This is the {} line in the file".format(count))
            print("The content for this line in the file is:", line, end="")
            print('############################')
    f.close()
    return

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
                        raise Exception("datarange should be a list,but now it is {}".format(type(value['datarange'])))
                    if len(value['datarange']) != 2:
                        raise Exception("datarange should have 2 numbers")
                    if value['datarange'][1] - value['datarange'][0] < kwargs['num']:
                        raise Exception(
                            "The range of random numbers you want to generate is smaller than the number of random numbers you want to generate")
                    if value['datarange'][1] - value['datarange'][0] <= 0:
                        raise Exception("The second number in your datarange is less than the first number")
                    else:
                        it = iter(value['datarange'])
                        tmp = random.randint(next(it), next(it))
                elif key == "float":
                    if isinstance(value['datarange'], tuple) == False:
                        raise Exception("datarange should be a list,but now it is {}".format(type(value['datarange'])))
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
                        raise Exception("datarange should be a str,but now it is {}".format(type(value['datarange'])))
                    elif value['strlen'] <= 0:
                        raise Exception("strlen should be greater than 0, but now it is less than or equal to 0")
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

def apply(filename):
    with open(filename, encoding="utf-8") as f:
        count = 0
        for line in f.readlines():
            count += 1
            data = line.strip()
            dic = (eval(data))
            result = structDataSampling(**dic)
            print('############################')
            print("test:Random number generated by reading the contents of the {} line of the file".format(count))
            print("The dict for this line in the file is:", line, end="")
            for item in result:
                print(item)
            print('############################')
    f.close()
    return

def getPrimeNumber(start,end):
    h = 0
    leap = 1
    for m in range(start, end):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % m,end=" ")
            h += 1
            if h % 10 == 0:
                print()
        leap = 1
    return h

def GetCity():       #Get user input of variable length
    city = []
    cityStr = input("Please enter the name of the city where you want to query the weather (press enter to exit):")
    while cityStr != "":
        city.append(cityStr)
        cityStr = input("Please enter the name of the city where you want to query the weather (press enter to exit):")
    return city
