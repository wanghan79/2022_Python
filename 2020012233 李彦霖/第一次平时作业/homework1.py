import random
import string


def structDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def txtFileReader(file):
    fr = open(file, 'r', encoding="utf-8")
    dic = {}
    for line in fr:
        list = line.strip().split(' ')
        if list[0] == 'str':
            dic[list[0]] = {list[1]: list[2], list[3]: int(list[4])}
            # print(dic)
        else:
            dic[list[0]] = {list[1]: [int(list[2]), int(list[3])]}
            # print(dic)
    return dic




def apply():
    res = structDataSampling(100, **txtFileReader('liyanlin1.txt'))
    for i in iter(res):
        print(i)

apply()
