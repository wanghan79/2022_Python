import random
from math import sqrt
from functools import wraps

'''
实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，其中模拟预测结果采用随机数生成函数作为被修饰函数
'''


def ACC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = list(fuc(*args, **kwargs))
        print(f"randomDate = {data}")
        num = len(data)
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
        tp = fp = tn = fn = 0
        for i in data:
            if i[0] & i[1]:
                tp += 1
            elif i[0] & (~i[1]):
                fp += 1
            elif (~i[0]) & (~i[1]):
                tn += 1
            elif (~i[0]) & i[1]:
                fn += 1
        MCC = (tp * tn) - (fp * fn) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        print(f"MCC = {MCC}")
        return data

    return wrap


@MCC
@ACC
def get_random_data(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                dt = iter(value['datarange'])
                tmp = random.randint(next(dt), next(dt))
            elif key == "float":
                dt = iter(value['datarange'])
                tmp = random.uniform(next(dt), next(dt))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == 'bool':
                cnt = value['count']
                for i in range(cnt):
                    tmp = random.randint(0, 1)
                    element.append(tmp)
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


para = {"num": 1000, "struct": {"bool": {"count": 2}}}

print(get_random_data(**para))
