import string
import random

def structDataSampling(*args, **kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs["struct"].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for word in range(value['len']))
            else :
                break
            element.append(tmp)
        result.append(element)
    return result

dist = {"num": 5,
        "struct": {"int": {"datarange": (0, 99)},
                   "float": {"datarange": (0, 999)},
                   "str": {"datarange": string.ascii_uppercase, "len": 20}
                   }
        }

file = open("dist.txt",'r')
read_para = file.read()
file.close()
para = eval(read_para)
print(structDataSampling(**para))


print(para['struct']['int']['datarange'])
print(para["struct"])
print(para['num'])