import math
import random
from functools import wraps
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import cProfile
import snakeviz.cli as cli
import pstats

"""
作业要求
改写平时作业三，采用生成器方式生成相应随机数
"""


class Generator(object):
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            if i == self.num:
                raise StopIteration
            elem = list()
            for key, val in self.struct.items():
                if key == "bool":
                    cnt = val["count"]
                    for idx in range(cnt):
                        elem.append(random.choice((True, False)))
                else:
                    print("Usage: Type Error!")
                    break
            yield elem


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
    generator = Generator(**kwargs)
    res = []
    for elem in generator:
        res.append(elem)
    return res


def main():
    data = {
        "num": 10,
        "struct": {
            "bool": {"count": 2},
        }
    }
    with ThreadPoolExecutor(max_workers=5) as pool:
        all_task = []
        for i in range(2, 6):
            task = pool.submit(generateRandomData, **data)
            global TP, TN, FP, FN
            TP = TN = FP = FN = 0
            data["num"] = int(data["num"] * i)
            all_task.append(task)
        for task in as_completed(all_task):
            print("done")


if __name__ == '__main__':
    filename = "res.prof"
    with cProfile.Profile() as pr:
        pr.enable()
        main()
        ps = pstats.Stats(pr)
    ps.dump_stats(filename=filename)
    cli.main([filename])
