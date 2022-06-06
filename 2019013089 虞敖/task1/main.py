import random


def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():     # 进入下一层索引
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


def apply():
    txt_file = open("mes.txt")
    para = eval(txt_file.read())
    result = structDataSampling(**para)
    for item in result:
        print(item)


apply()