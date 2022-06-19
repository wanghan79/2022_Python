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


file = open('test', 'r')
read_test = file.read()
file.close()
dic = eval(read_test)
print(dic)
print(structDataSampling(**dic))




