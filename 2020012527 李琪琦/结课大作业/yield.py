#通过修饰器（类或者函数修饰器）来修饰生成结果的函数
import math
import random


def ACC(func):#正确率统计（精度统计）
    def wrapper(*args, **kwargs):#使用万能参数，可接受所有类型被修饰函数的参数
        count = num = 0
        results = []
        for i in func(*args, **kwargs):
            results.append(i)
            if i[0] == i[1]:
                count += 1
            num += 1
        acc = count / num
        print("ACC : {}".format(acc))
        return results
    return wrapper


def MCC(func):#马修斯相关系数的统计（对二分类结果进行）
    def wrapper(*args, **kwargs):#使用万能参数
        results = []
        TP = FP = TN = FN = 0
        for i in func(*args, **kwargs):#i[0]是预测情况，i[1]是真实情况
            results.append(i)
            if (i[0] is True) :
                if (i[1] is True):
                    TP += 1
            if (i[0] is True) :
                if (i[1] is False):
                    FP += 1
            if (i[0] is False) :
                if (i[1] is True):
                    FN += 1
            if (i[0] is False) :
                if (i[1] is False):
                    TN += 1
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FP) * (TN + FP) * (TN + FN))
        print("MCC : {}".format(mcc))
        return results
    return wrapper


@MCC
@ACC
def structDataSampling(**kwargs):
    #result = list()
    for i in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
                element.append(tmp)
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
                element.append(tmp)
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
            elif key == "bool":
                for ith in range(value["num"]):
                    tmp = random.choice((True, False))
                    element.append(tmp)
            else:
                break
        yield element


if __name__ == '__main__':
    args = {'num': 10000, 'struct': {'bool': {"num": 2}}}
    format(structDataSampling(**args))