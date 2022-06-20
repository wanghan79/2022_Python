import string
import random
import os
import sys

'''
para = {
    "num": 5,
    "struct": {
        "int": {"datarange": (0, 100)},
        "float": {"datarange": (0, 10000)},
        "str": {"datarange": string.ascii_uppercase, "len": 50},
        # "bool":
    }
}
'''


def structDataSampling(num, **struct):
    """
    :param num: numbers of Datas
    :param struct: struct of Datas
    :return: list of Datas
    """
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in struct.items():
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
        result.append(element)
    return result


filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]
with open(filePath + '\\para.txt') as f:
    para = eval(f.read())

result = structDataSampling(para['num'], **para['struct'])
for item in result:
    print(item)
