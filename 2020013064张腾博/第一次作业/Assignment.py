import random
import string

def structDataSampling(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    result = list()
    for index in range(0, kwargs['num']):
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
        result.append(element)
    return result


def apply():
    fr = open("test.txt", 'r')
    dic = eval(fr.read())  # 读取的str转换为字典
    result = structDataSampling(**dic)
    for item in result:
        print(item)
    fr.close()


apply()
