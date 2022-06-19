"""
   Author: Zhou
   Purpose: Python task 01
   Created: {2022/06/01}
"""
import random
import string

def structDataSamping(**kwargs):
    result=list()
    for index in range(0,kwargs['num']):
        element=list()
        for key,value in kwargs['struct'].items():
             if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
             elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
             elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
             else:
                  break
             element.append(tmp)
        result.append(element)
    return result

def dataScreening():
    pass

def apply():
   file=open('data.txt')
   dic=eval(file.read())
   result=structDataSamping(**dic)
   for item in result:
       print(item)
apply()