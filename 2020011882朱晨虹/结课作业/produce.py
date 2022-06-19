"""
li
pass
2022 6/05
"""
import math
import random


def ACC():
    def dec(func):
        def wrapper(*args, **kwargs):
            tmplst = list(*args)
            tp = fp = fn = tn = 0
            for item in tmplst:
                if item[0] == 1 & item[1] == 1:
                    tp = tp + 1
                elif item[0] == 1 & item[1] == 0:
                    fp = fp + 1
                elif item[0] == 0 & item[1] == 1:
                    fn = fn + 1
                elif item[0] == 0 & item[1] == 0:
                    tn = tn + 1
            acc = (tp + tn) / len(tmplst)
            print("ACC:", acc)
            return func(*args, **kwargs)
        return wrapper
    return dec


def MCC():
    def dec(func):
        def wrapper(*args, **kwargs):
            tmplist = list(*args)
            tp = fp = fn = tn = 0
            for item in tmplist:
                if item[0] == 1 & item[1] == 1:
                    tp = tp + 1
                elif item[0] == 1 & item[1] == 0:
                    fp = fp + 1
                elif item[0] == 0 & item[1] == 1:
                    fn = fn + 1
                elif item[0] == 0 & item[1] == 0:
                    tn = tn + 1
            t = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
            mcc = (tp * tn - fp * fn) / math.sqrt(t)
            print("MCC:", mcc)
            return func(*args, **kwargs)
        return wrapper
    return dec


def dataSampling(num, **kwargs):
    '''

    :param struct:
    :return: 随机生成num个0，1二元数组
    '''
    result = list()
    for i in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == 'bool':
                for t in range(0, 2):
                    it = iter(value['datarange'])
                    tmp = bool(random.randint(next(it), next(it)))
                    element.append(tmp)
            else:
                break
        result.append(element)
        yield element   # 生成器
    # print(result, len(result))
    return result


@ACC()
@MCC()
def pred(recieve):
    return recieve


struct = {"bool":{"datarange":(0,2)}}
# reclist = dataSampling(100000, **struct)
# pred(reclist)

# 打印随机数，函数dataSampling(num, **kwargs)可迭代
for item in dataSampling(10000, **struct):
    print(item)
