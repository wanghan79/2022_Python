import json
import random
import string

def function(**kwargs):
    result = list()
    for item in range(0, kwargs['num']):
        for element in kwargs['struct'].items():
            elementTwo = list()
            for key, value in kwargs['struct'].items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value["datarange"])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = " ".join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    break
                elementTwo.append(tmp)
            result.append(elementTwo)
        return result

fr = open("homeworkOne.txt", 'r+')
dic = eval(fr.read())   #读取的str转换为字典
fr.close()
print(function(**dic))


