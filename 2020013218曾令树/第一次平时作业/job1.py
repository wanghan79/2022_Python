import random
import string
def generateRandom(**kargs):
    result = list()
    num = kargs["num"]
    struct = kargs["struct"]
    for i in range(num):
        element = list()
        for key, val in struct.items():
            if key == "int":
                it = iter(val["range"])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(val["range"])
                element.append(random.uniform(next(it), next(it)))
            elif key =="str":
                strRange = val["range"]
                strLength = val["length"]
                string = ""
                for j in range(strLength):
                    string+=random.choice(strRange)
                element.append(string)
            else:
                element.append("未知类型")
        result.append(element)
    return result
argument = {"num":5, "struct":{"int":{"range":(10,20)}, "float":{"range":(100,200)}, "str":{"range":string.ascii_uppercase, "length":10}}}

# ans = generateRandom(**argument)
# for elem in ans:
#     print(elem)

with open("myStruct.txt", "r") as f:
    structText = f.readlines()
num = int(structText[0].split()[0])
cin = {}
cin["num"] = num
struct = {}
for line in structText:
    words = line.split()
    dataType = words[0]
    if dataType == "int":
        info = {}
        left = int(words[1]); right = int (words[2])
        info["range"] = (left, right)
        struct["int"] = info
    elif dataType == "float":
        info = {}
        left = float(words[1]); right = float(words[2])
        info["range"] = (left, right)
        struct["float"] = info
    elif dataType == "str":
        info = {}
        info["range"] = words[1]
        info["length"] = int(words[2])
        struct["str"] = info
    else:
        continue
cin["struct"] = struct
ans = generateRandom(**cin)
for elem in ans:
    print(elem)

