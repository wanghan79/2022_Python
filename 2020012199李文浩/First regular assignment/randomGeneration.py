'''
Created on April 22, 2022
@author: Ivan Li
'''

# import related packages
import random
import string
import argparse as arg

# generate random number
def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
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

# return {'datarange', 'len'(optional)}
def loadDataType(data, dataType):
    info = {}
    if dataType == str:
        info['datarange'] = dataType(data[1])
        info['len'] = int(data[2])
    else:
        info['datarange'] = (dataType(data[1]), dataType(data[2]))
    return info

# return keyword parameters
def readParameters(filePath):
    with open(filePath, 'r') as f:
        myStruct = f.readlines()
        para = {}
        para['num'] = int(myStruct[0])
        para['struct'] = {}
        for line in myStruct[1: ]:
            parameter = line.split()
            dataType = parameter[0]
            para['struct'][dataType] = loadDataType(parameter, eval(dataType))
    return para

if __name__ == '__main__':
    print(__doc__)
    filePath = 'myStruct.txt'
    # {'num': 5, 'struct': {'int': {'datarange': (0, 100)}, 'float': {'datarange': (0.0, 10000.0)}, 'str': {'datarange': 'abcdefghijklmnopqrstuvwxyz', 'len': 30}}}
    para = readParameters(filePath)
    ans = structDataSampling(**para)
    for elem in ans:
        print(elem)