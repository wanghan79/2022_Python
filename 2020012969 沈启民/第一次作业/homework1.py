import string
import random

para = {"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}

def structDataSampling(*args, **kwargs):
    result = list()
    for item in range(0,kwargs['num']):
        element = list()
        for key,value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result



print(structDataSampling(**para))

def apply():
    exfile = open("data.txt")
    para = eval(exfile.read())
    result = structDataSampling(**para)
    for item in result:
        print(item)


apply()
