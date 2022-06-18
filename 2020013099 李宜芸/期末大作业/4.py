import json
import math
import random


class ResultAnalysis:
    def __init__(self, call_name):
        self.__func = call_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            if results is None:
                return None
            if self.__func == "ACC":
                return self.ACC(results)
            elif self.__func == "MCC":
                return self.MCC(results)
        return wrapper

    def ACC(self, data):
        """
        accuracy = (TP + FN) / N
        :param data:
        :return:
        """
        right = 0
        for one in data:
            if one[0] == one[2]:
                right += 1
        acc = right / len(data)    # 准确率
        return acc

    def MCC(self, data):
        """
        TP:预测为真，实际为真
        TN:预测为假，实际为真
        FP:预测为真，实际为假
        FN:预测为假，实际为假
        N = TN + TP + FN + FP
        S = (TP + FN) / N
        P = (TP + FP) / N
        MCC = (TP/N - S*P) / sqrt(PS(1-S)(1-P))
        :param data:
        :return:
        """
        TP, TN, FP, FN = 0, 0, 0, 0
        for one in data:
            if one[0] == 1 and one[2] == 1:
                TP += 1
            elif one[0] == 0 and one[2] == 1:
                TN += 1
            elif one[0] == 1 and one[2] == 0:
                FP += 1
            elif one[0] == 0 and one[2] == 0:
                FN += 1
        # print(TP, TN, FP, FN)
        N = TP + TN + FP + FN
        S = (TP + FN) / N
        P = (TP + FP) / N
        MCC = (TP / N - S * P) / math.sqrt(P*S*(1 - S)*(1 - P))
        return MCC


def read_data():
    path = './data.json'
    with open(path, 'r') as f:
        data = json.load(f)
        return data["struct"]


def mygenerator(num, **kwargs):
    '''
    数据生成器
    :param num:生成数据的个数
    :param kwargs: 字典参数
    :return:
    '''
    count = 0
    while count < num:
        element = list()
        for key, value in kwargs.items():
            if key == "predict":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "true":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                raise Exception("The type of data is wrong")
            element.append(tmp)
        if len(element) == 3:
            yield element
        else:
            raise Exception("Data Wrong")
        count += 1


@ResultAnalysis("ACC")
def get_acc_results(num, **kwargs):
    res = []
    tmp_generator = mygenerator(num, **kwargs)
    for value in tmp_generator:
        res.append(value)

    return res

@ResultAnalysis("MCC")
def get_mcc_results(num, **kwargs):
    res = []
    tmp_generator = mygenerator(num, **kwargs)
    for value in tmp_generator:
        res.append(value)

    return res

para = read_data()

acc = get_acc_results(10000, **para)
mcc = get_mcc_results(10000, **para)
print(acc, mcc)

