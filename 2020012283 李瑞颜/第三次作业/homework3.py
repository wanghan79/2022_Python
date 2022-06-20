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
    # 计算ACC
    def ACC(self, data):
        correct = 0
        sum = len(data)
        for index, sample in enumerate(data): # 使用enumerate生成索引序列，同时列出数据和数据下标
            if sample[0] == sample[1]:
                correct += 1
        ans = correct / sum

        return ans
    # 计算MCC
    def MCC(self, data):
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for index, sample in enumerate(data):
            if sample[0] == 1 and sample[1] == 1:
                TP += 1
            elif sample[0] == 1 and sample[1] == 0:
                FN += 1
            elif sample[0] == 0 and sample[1] == 1:
                FP += 1
            elif sample[0] == 0 and sample[1] == 0:
                TN += 1
        denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        if denominator == 0:
            ans = 0
        else:
            ans = (TP * TN - FP * FN) / denominator

        return ans


# 函数修饰器,用来传入static的值
def Result_Analysis(static):
    def wrapper(func):
        return ResultAnalysis(func, static)

    return wrapper



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
                for i in range(value['number']):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                break
            result.append(tmp)
    return result


@Result_Analysis("MCC")
def structDataSampling_MCC(**kwargs):

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
                for i in range(value['number']):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                break
            result.append(tmp)
    return result


para = {"num": 5000, "struct": {"bool": { "number": 2}}}

accAns = structDataSampling_ACC(**para)
print(accAns)

mccAns = structDataSampling_MCC(**para)
print(mccAns)
