import random
from math import sqrt


def ACC(f):
    def wrap(*args, **kwargs):
        count = 0
        data = f(*args, **kwargs)
        for i in range(len(data)):
            if data[i][0] == data[i][1]:
                count += 1
        print("ACC = {}".format(count / len(data)))
        return data
    return wrap


def MCC(f):
    def wrap(*args, **kwargs):
        data = f(*args, **kwargs)
        tp, fp, tn, fn = 0, 0, 0, 0
        for i in data:
            if i[0] & i[1]:
                tp += 1
            elif i[0] & (~i[1]):
                fp += 1
            elif ~i[0] & ~i[1]:
                tn += 1
            elif ~i[0] & i[1]:
                fn += 1
        MCC = ((tp * tn) - (fp * fn)) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        print("MCC = {}".format(MCC))
        return data
    return wrap


@MCC
@ACC
def getRandomData(**kwargs):
    result = []
    for i in range(0, kwargs['num']):
        element = []
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                element.append(''.join(random.choice(value['datarange']) for item in range(value['len'])))
            elif key == "bool":
                for item in range(value["num"]):
                    element.append(random.choice((True, False)))
            else:
                break
        result.append(element)
    return result


if __name__ == '__main__':
    args = {'num': 10000, 'struct': {'bool': {"num": 2}}}
    format(getRandomData(**args))