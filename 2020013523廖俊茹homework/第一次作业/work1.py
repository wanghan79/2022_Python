import random

def structDataSampling(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    result = list()
    for index in range(0,kwargs['num']):
        for ite in kwargs['struct'].items():#注意注意！！！ite是元组
            element = list()
            for i in ite:
                if ite[0] == "int":
                    it = iter(ite[1]['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif ite[0] == "float":
                    it = iter(ite[1]['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif ite[0] == "str":
                    tmp = ''.join(random.SystemRandom().choice(ite[1]['datarange']) for _ in range(ite[1]['len']))
                else:
                    break
                element.append(tmp)
            result.append(element)
    return result


import string
para = {"num": 5, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)}, "str": {"datarange": string.ascii_uppercase, "len": 50}}}
def apply():
    # struct ={"num": 5,"struct" = {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)}, "str": {"datarange": string.ascii_uppercase, "len": 50}}
    result = structDataSampling(**para)
    for i in result:
        print(i)
apply()