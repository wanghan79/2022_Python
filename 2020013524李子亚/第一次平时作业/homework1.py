import random
import string


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
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


para = {"num": 5,
        "struct": {"int": {"datarange": (0, 1000)},
                   "float": {"datarange": (0, 1000)},
                   "str": {"datarange": string.ascii_uppercase, "len": 15}
                   }
        }

anw = structDataSampling(**para)

print(anw)

with open("homework1.txt", "w", encoding='utf-8') as f:
    for i in anw:
        f.write(str(i))
        f.write('\n')
f.close()
