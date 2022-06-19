import string
import random

# para = {"num": 5, "struct":{"int": {"datarange":(0,100)}, "float": {"datarange":(0,10)}, "str": {"datarange":string.ascii_uppercase,"len":5}}}

#生成随机数
def structDataSampling(**kwargs):
    result = list()
    num = kwargs["num"] #生成具体的个数
    struct = kwargs["struct"] #生成struct中对应元素类型的随机数
    for item in range(num):
        element = list()
        for key, value in struct.items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                strRange = value["datarange"]
                strLength = value["len"]
                string = ""
                for i in range(strLength):
                    string += random.choice(strRange)
                element.append(string)
            else:
                break
        result.append(element)
    return result

# result = structDataSampling(**para)
# print(result)


#读取外部文件
with open("para.txt", "r") as f:
    structText = f.readlines()

num = int(structText[0].split()[0])  #读取文件个数，如para字典中的num
cin = {}
cin["num"] = num
struct = {}
for line in structText: #逐行读取
    words = line.split()
    dataType = words[0]
    if dataType == "int":
        info = {}
        left = int(words[1])
        right = int (words[2])
        info["datarange"] = (left, right)
        struct["int"] = info
    elif dataType == "float":
        info = {}
        left = float(words[1])
        right = float(words[2])
        info["datarange"] = (left, right)
        struct["float"] = info
    elif dataType == "str":
        info = {}
        info["datarange"] = words[1]
        info["len"] = int(words[2])
        struct["str"] = info
    else:
        continue
cin["struct"] = struct

answer = structDataSampling(**cin)
for elem in answer:
    print(elem)