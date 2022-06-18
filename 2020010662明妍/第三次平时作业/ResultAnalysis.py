import math
import random


def ACC(func):
    def wrap(*args, **kwargs):
        count = 0
        result = func(*args, **kwargs)
        n = len(result)
        for i in range(n):
            if result[i][0] == result[i][1]:
                count += 1
        acc = count / n
        print("ACC : %f" % acc)
        return result

    return wrap


def MCC(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        tp = fp = tn = fn = 0
        for i in result:
            if i[0] == 1 & i[1] == 1:
                tp += 1
            elif i[0] == 1 & i[1] == 0:
                fp += 1
            elif i[0] == 0 & i[1] == 0:
                tn += 1
            elif i[0] == 0 & i[1] == 1:
                fn += 1
        m = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        mcc = ((tp * tn) - (fp * fn)) / m
        print("MCC : %f" % mcc)
        return result

    return wrap


@MCC
@ACC
def getRandomData(**kwargs):
    result = list()
    for i in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                element.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    element.append(random.choice((True, False)))
            else:
                break
        result.append(element)
    return result


if __name__ == '__main__':
    argument = {'num': 1000, 'struct': {'bool': {"num": 2}}}
    format(getRandomData(**argument))
