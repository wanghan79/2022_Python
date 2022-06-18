import random

def ACC(fun):
    def wrap(*args, **kwargs):
        count = 0
        data = fun(*args, **kwargs)
        n = len(data)
        for i in range(n):
            if data[i][0] == data[i][1]:
                count += 1
        acc = count / n
        print("ACC : {}".format(acc))
        return data
    return wrap

def MCC(fun):
    def wrap(*args, **kwargs):
        data = fun(*args, **kwargs)
        TP, FP, TN, FN = 0, 0, 0, 0
        for i in data:
            if i[0] & i[1]:
                TP += 1
            elif i[0] & (~i[1]):
                FP += 1
            elif ~i[0] & ~i[1]:
                TN += 1
            elif ~i[0] & i[1]:
                FN += 1
        mcc = ((TP * TN) - (FP * FN)) / ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))**0.5
        print("MCC : {}".format(mcc))
        return data
    return wrap

@MCC
@ACC
def getRandomData(**keys):
    samples = []
    for i in range(0, keys['num']):
        sample = []
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                sample.append(random.randint(next(daterange), next(daterange)))
            elif key == "float":
                daterange = iter(value['datarange'])
                sample.append(random.uniform(next(daterange), next(daterange)))
            elif key == "str":
                sample.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    sample.append(random.choice((True, False)))
            else:
                break
        samples.append(sample)
    return samples

if __name__ == '__main__':
    args = {'num': 100, 'struct': {'bool': {"num": 2}}}
    print("PredictData: {}".format(getRandomData(**args)))