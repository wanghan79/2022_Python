import random
import string
def generateRandom(**kargs):
    result = list()
    num = kargs["num"]
    struct = kargs["struct"]
    for i in range(0,num):
        element = list()
        for key, val in struct.items():
            if key == "int":
                it = iter(val["range"])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(val["range"])
                element.append(random.uniform(next(it), next(it)))
            elif key =="str":
                element.append(''.join(random.SystemRandom().choice(val['range']) for _ in range(val['len'])))
            else:
                element.append("未知类型")
        result.append(element)
    return result

file = open("myStruct.txt",'r') #读取文件
read_para = file.read()
file.close()
para = eval(read_para)
print(generateRandom(**para))
