'''
Created on May 20, 2022
@author: Ivan Li
'''

# import related packages
import math
import random
import string
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import matthews_corrcoef

# a decorator to analysis the results
class ResultAnalysis:
    def __init__(self, func):
        self.__func = func

    def __call__(self, **kwargs):
        results = self.__func( **kwargs)
        if results is None:
            return None
        else:
            description = self.result_description(results)
            print('ACC: ' + str(self.acc(description)))
            print('MCC: ' + str(self.mcc(description)))

    def result_description(self, results):
        description = {}
        TP = TN = FP = FN = 0
        for result in results:
            if (result[0][0] is True) and (result[0][1] is True):
                TP += 1
            elif (result[0][0] is True) and (result[0][1] is False):
                FN += 1
            elif (result[0][0] is False) and (result[0][1] is True):
                FP += 1
            elif (result[0][0] is False) and (result[0][1] is False):
                TN += 1
            else:
                pass
        return [TP, TN, FP, FN]

    # acc = (TP + TN) / (TP + TN + FP + FN)
    def acc(self, description):
        # accuracy_score(y_true=, y_pred=)
        TP, TN, FP, FN = description
        return (TP + TN) / (TP + FP + TN + FN)

    # mcc = (TP + TN) / (TP + TN + FP + FN)
    def mcc(self, description):
        # matthews_corrcoef(y_true=, y_pred=)
        TP, TN, FP, FN = description
        numerator = (TP * TN) - (FP * FN)
        denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        if (denominator == 0):
            denominator = 1
        return numerator / denominator

# generate random number with ResultAnalysis decorator
@ResultAnalysis
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
            elif key == "bool":
                tmp = random.choices(value['datarange'], k=2)
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
    elif dataType == bool:
        info['datarange'] = (dataType(int(data[1])), dataType(int(data[2])))
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
    para = readParameters(filePath)
    ans = structDataSampling(**para)