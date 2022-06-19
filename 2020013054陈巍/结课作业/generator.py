import random
from math import sqrt
from functools import wraps


def ACC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):# *args 可以传数量随意的位置参数；**kwargs 可以传默认参数
        data = list(fuc(*args, **kwargs))
        print(f"randomDate = {data}")
        num=len(data)
        count = 0
        for i in range(num):
            if data[i][0] == data[i][1]:
                count += 1
        print(f"ACC = {count / num}")
        return data
    return wrap

def MCC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = list(fuc(*args, **kwargs))
        tp, fp, tn, fn = 0, 0, 0, 0
        for item in data:
            if item[0] & item[1]:
                tp += 1
            elif item[0] & (~item[1]):
                fp += 1
            elif ~item[0] & ~item[1]:
                tn += 1
            elif ~item[0] & item[1]:
                fn += 1
        numerator = (tp * tn) - (fp * fn)
        denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        MCC = numerator / denominator
        print(f"MCC = {MCC}")
        return data
    return wrap

@MCC
@ACC
def getRandomData(**dic):
    for i in range(0, dic['num']):
        for key, value in dic['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                yield random.randint(next(daterange), next(daterange))
            elif key == "float":
                daterange = iter(value['datarange'])
                yield random.uniform(next(daterange), next(daterange))
            elif key == "str":
                yield ''.join(random.choice(value['datarange']) for i in range(value['len']))
            elif key == "bool":
                yield [random.choice((True, False)) for _ in range(value["num"])]
            else:
                break


num = random.randint(1000,10000)
args = {'num':num , 'struct': {'bool': {"num": 2}}}
getRandomData(**args)

