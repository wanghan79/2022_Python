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
        "struct": {"int": {"datarange": (0, 100)},
                   "float": {"datarange": (0, 1000)},
                   "str": {"datarange": string.ascii_uppercase, "len": 10}
                   }
        }

anw = structDataSampling(**para)

print(anw)

with open("project1.txt", "w") as f:
    n = 1
    for fist_line in anw:
        f.write("---第" + str(n) + "次---" + '\n')
        for second_line in fist_line:
            f.write(str(second_line) + '\n')
        f.write('\n')
        n = n + 1

f.close()
