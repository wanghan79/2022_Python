"""
     Author  : Jiaxuan Jiang
     File    : finalWork.py
     describe: 实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，其中模拟预测结果采用随机数生成函数作为被修饰函数，采用生成器方式生成相应随机数
"""


import math
import random


class ResultAnalysis:

    def __init__(self, func):
        self.__func = func

    def __call__(self, **kwargs):
        results = self.__func(**kwargs)
        if results is None:
            return None
        else:
            TP, TN, FP, FN = self.dataGenerate(results)
            self.ACC(TP, TN, FP, FN)
            self.MCC(TP, TN, FP, FN)


    def dataGenerate(self,data):

        TP = 0
        FN = 0
        FP = 0
        TN = 0

        for i, element in enumerate(data):  # 使用yield关键字后，被修饰函数返回的是可迭代对象，故这里使用enumerate进行迭代
            for sample in element:
                if sample[0] == 1 and sample[1] == 1:
                    TP += 1
                elif sample[0] == 1 and sample[1] == 0:
                    FN += 1
                elif sample[0] == 0 and sample[1] == 1:
                    FP += 1
                elif sample[0] == 0 and sample[1] == 0:
                    TN += 1
        return TP,FN,FP,TN

    def ACC(self, TP, TN, FP, FN):
        ans = (TP + TN) / (TP + TN + FP + FN)
        print("ACC = %f" %ans)

    def MCC(self, TP, TN, FP, FN):

        ans = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (FN + TP) * (FN + TN) * (FP + TN))
        print("MCC = %f" %ans)


@ResultAnalysis
def structDataSampling(**kwargs):
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

    yield result


if __name__ == "__main__":


    data = {"num": 10000, "struct": {"bool": {"number": 2}}}


    structDataSampling(**data)



