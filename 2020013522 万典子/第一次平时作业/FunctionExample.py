import string
import random

para = {"num": 10, "struct":{"float" : {"datarange": (0,10000)}, "str": {"datarange": string.ascii_letters, "len": 8}, "int": {"datarange": [0, 10000]}}}

def structDataSampling(**kwargs):
    results = list()
    for item in range(0,kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        results.append(element)
    return results


def apply():
    result = structDataSampling(**para)
    for i in result:
        print(i)

apply()
