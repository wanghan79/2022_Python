import random


def structDataSampling1(**kwargs):
    result = list()
    for key, value in kwargs.items():
        if key == 'num':
            count = value
            break
    for index in range(0, count):
        element = list()
        for key, value in kwargs.items():
            if key == 'num':
                continue
            elif key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.choice(value['datarange']) for _ in range(value['length']))
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
        if list[0] == 'num':
            dic[list[0]] = int(list[1])
        elif list[0] == 'str':
            dic[list[0]] = {list[1]: list[2], list[3]: int(list[4])}
        else:
            dic[list[0]] = {list[1]: [int(list[2]), int(list[3])]}
    return dic


def apply():
    res = structDataSampling1(**txtFileReader('rcg.txt'))
    for i in iter(res):
        print(i)
    print("打印完毕！！！！")


apply()
