""" 
    @Time    : 2022/6/10 11:22
    @Author  : Jiaxuan Jiang
    @Email   : 6812624@qq.com
    @File    : homework4.py
    @Software: PyCharm
"""
import random
import math


class ResultAnalysis:
    def __init__(self, func, static="ACC"):
        self.__func = func
        self.__static = static

    def __call__(self, *args, **kwargs):
        results = self.__func(*args, **kwargs)
        if results is None:
            return None
        if self.__static == "ACC":
            return self.ACC(results)
        elif self.__static == "MCC":
            return self.MCC(results)
        else:
            pass

    def ACC(self, data):
        # correctPrediction = 0
        # sumOfSample = len(data) 由于采用生成器方式生成相应随机数，data为生成器类型，不支持len(),所以会出现object of type 'generator' has no len()错误，这是相比于作业3修改的地方
        TP = 0  # truePositive
        TN = 0  # trueNegative
        FP = 0  # falsePositive
        FN = 0  # falseNegative
        for index, it in enumerate(data):  # 由于使用了yield关键字，相比于作业3修改了循环
            for sample in it:
                if sample[0] == 1 and sample[1] == 1:
                    TP += 1
                elif sample[0] == 1 and sample[1] == 0:
                    FN += 1
                elif sample[0] == 0 and sample[1] == 1:
                    FP += 1
                elif sample[0] == 0 and sample[1] == 0:
                    TN += 1
        print("precision calculation:")
        accuracy = (TP + TN) / (TP + TN + FP + FN)
        return accuracy

    def MCC(self, data):
        TP = 0  # truePositive
        TN = 0  # trueNegative
        FP = 0  # falsePositive
        FN = 0  # falseNegative
        for index, it in enumerate(data):  # 由于使用了yield关键字，相比于作业3修改了循环
            for sample in it:
                if sample[0] == 1 and sample[1] == 1:
                    TP += 1
                elif sample[0] == 1 and sample[1] == 0:
                    FN += 1
                elif sample[0] == 0 and sample[1] == 1:
                    FP += 1
                elif sample[0] == 0 and sample[1] == 0:
                    TN += 1
        print("Matthew correlation coefficient calculation:")
        matthewsScore = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (FN + TP) * (FN + TN) * (FP + TN))
        return matthewsScore


# 由于不能直接通过类修饰器直接这样@ResultAnalysis("ACC" or "MCC")传参数，多写了一个函数修饰器传入static的值
def Result_Analysis(static):
    def wrapper(func):
        return ResultAnalysis(func, static)

    return wrapper


# 可以写两个被修饰函数一个计算ACC 一个计算MCC
@Result_Analysis("ACC")
def structDataSampling_ACC(**kwargs):
    """

    :param kwargs:
    :return:
    """
    result = list()
    for index in range(kwargs['num']):
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['dataRange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['dataRange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                it = iter(value['dataRange'])
                tmp = ''.join(random.SystemRandom().choice(value['dataRange']) for _ in range(8))
            elif key == "bool":
                tmp = []
                for i in range(value['cnt']):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                break
            result.append(tmp)
    yield result


@Result_Analysis("MCC")
def structDataSampling_MCC(**kwargs):
    """

    :param kwargs:
    :return:
    """
    result = list()
    for index in range(kwargs['num']):
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['dataRange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['dataRange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                it = iter(value['dataRange'])
                tmp = ''.join(random.SystemRandom().choice(value['dataRange']) for _ in range(8))
            elif key == "bool":
                tmp = []
                for i in range(value['cnt']):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                break
            result.append(tmp)
    yield result


# 生成10000个二元组(bool, bool)，防止生成二元组数量过少，而导致计算马修相关系数时分母出现0的问题
para = {"num": 10000, "struct": {"bool": {"dataRange": (True, False), "cnt": 2}}}  # 生成10000个二元组(bool, bool)

accResult = structDataSampling_ACC(**para)
print(accResult)

mccResult = structDataSampling_MCC(**para)
print(mccResult)
