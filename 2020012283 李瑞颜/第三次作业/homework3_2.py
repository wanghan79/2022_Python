"""
    Author  : Ruiyan Li
    File    : homework3_2.py
    describe: 实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，其中模拟预测结果采用随机数生成函数作为被修饰函数，采用生成器方式生成相应随机数
              此文件使用函数嵌套实现修饰器，homework3.py使用类实现修饰器
"""
import random
import math
from functools import wraps


def Decorator(level):

    # 1.ACC计算方法
    def ACC(data):
        correct = 0
        sum = len(data)
        for i, element in enumerate(data):  # 使用enumerate生成索引序列，同时列出数据和数据下标
            if element[0] == element[1]:
                correct += 1
        accuracy = correct / sum
        print("ACC =%f" % accuracy)

    # 2.MCC计算方法
    def MCC(data):
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for i, element in enumerate(data):
            if element[0] == 1 and element[1] == 1:
                TP += 1
            elif element[0] == 1 and element[1] == 0:
                FN += 1
            elif element[0] == 0 and element[1] == 1:
                FP += 1
            elif element[0] == 0 and element[1] == 0:
                TN += 1
        denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        if denominator == 0:
            ans = 0
        else:
            ans = (TP * TN - FP * FN) / denominator
        print("MCC = %f" %ans)

    # 3. 嵌套函数，在得到原函数的结果后，根据level为ACC或MCC进行响应的计算并得出结果
    def wrap1(func):
        @wraps(func)
        def wrap2(**kwargs):
            ans = func(**kwargs)

            if level == "ACC":
                ACC(ans)
            else :
                MCC(ans)
        return wrap2
    return wrap1


@Decorator("ACC")
def structDataSampling_ACC(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):

        for key, value in kwargs['struct'].items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                tmp = []
                for i in range(value['number']):
                    tmp.append(random.choice((0, 1)))

                tmp = tuple(tmp)

            else:
                break
            result.append(tmp)

    return result


@Decorator("MCC")
def structDataSampling_MCC(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):

        for key, value in kwargs['struct'].items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                tmp = []
                for i in range(value['number']):
                    tmp.append(random.choice((0, 1)))

                tmp = tuple(tmp)

            else:
                break
            result.append(tmp)

    return result


para = {"num": 10000, "struct": {"bool": { "number": 2}}}

structDataSampling_ACC(**para)

structDataSampling_MCC(**para)
