import math
import random
from functools import wraps
import cProfile
import snakeviz.cli as cli
import pstats

"""
作业要求
实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，其中模拟预测结果采用随机数生成函数作为被修饰函数
"""

TP, TN, FP, FN = 0, 0, 0, 0


def init():
    """
    初始化TP, TN, FP, FN
    """

    def calc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global TP, TN, FP, FN
            ret = func(*args, **kwargs)
            for pair in ret:
                if pair[0] == 1:
                    TP = TP + 1 if pair[1] == 1 else TP
                    FP = FP + 1 if pair[1] == 0 else FP
                else:
                    FN = FN + 1 if pair[1] == 1 else FN
                    TN = TN + 1 if pair[1] == 0 else TN
            return ret

        return wrapper

    return calc


def ACC():
    """
    ACC = (TP + TN) / (TP + TN + FP + FN)
    """

    def calc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            print("Acc = {:.2%}".format((TP + TN) / (TP + TN + FP + FN)))
            return ret

        return wrapper

    return calc


def MCC():
    """
    MCC = [(TP * TN) - (FP * FN)] / sqrt[(TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)]
    """

    def calc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            frac = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = 0 if frac == 0 else (TP * TN - FP * FN) / frac
            print("MCC = {:.2%}".format(mcc))
            return ret

        return wrapper

    return calc


@ACC()
@MCC()
@init()
def generateRandomData(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs["struct"].items():
            if key == "num":
                continue
            if key == "bool":
                cnt = value["count"]
                for i in range(cnt):
                    element.append(random.choice((True, False)))
            else:
                print("Usage: Data Error!")
                break
        result.append(element)
    return result


def main():
    data = {
        "num": 10000,
        "struct": {
            "bool": {"count": 2},
        }
    }
    generateRandomData(**data)


if __name__ == '__main__':
    filename = "res.prof"
    with cProfile.Profile() as pr:
        pr.enable()
        main()
        ps = pstats.Stats(pr)
    ps.dump_stats(filename=filename)
    cli.main([filename])
