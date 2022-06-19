import random
from math import sqrt
from functools import wraps


def ACC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):# *args 可以传数量随意的位置参数；**kwargs 可以传默认参数
        data = fuc(*args, **kwargs)
        length=len(data)
        count = 0
        for i in range(length):
            if data[i][0] == data[i][1]:
                count += 1
        print(f"ACC = {count / num}")
       # print(f"ACC_data:{data}")
        return data

    return wrap

def MCC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = fuc(*args, **kwargs)
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
      #  print(f"MCC_data:{data}")
        return data
    return wrap

@ACC
def AccSimu(num):
    list = []
    for i in range(num):
        item = [random.choice([True, False]), random.choice([True, False])]
        list.append(item)
 #   print(f"ACC:{list}")
    return list

@MCC
def MccSimu(num):
    list = []
    for i in range(num):
        item = [random.choice([True, False]), random.choice([True, False])]
        list.append(item)
  #  print(f"MCC:{list}")
    return list


num = random.randint(1000,10000)
AccSimu(num)
MccSimu(num)
