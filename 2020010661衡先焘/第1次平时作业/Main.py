import random

print("===第1次平时作业===")

def generateRandom(num, **struct):
    if num <= 0:
        print("num = ", num, "num must > 0")
        return
    result = list()
    for i in range(num):
        element = list()
        for key, val in struct.items():
            if key == "int":
                it = iter(val["range"])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(val["range"])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                strRange = val["range"]
                strLength = val["length"]
                string = ""
                for j in range(strLength):
                    string += random.choice(strRange)
                element.append(string)
            else:
                element.append("未知类型")
        result.append(element)
    return result


with open("test.txt", "r", encoding='utf-8') as f:
    structText = f.readlines()

cin = {}
for line in structText:
    if line.startswith("###########"):
        print("读取文件完成")
        break
    words = line.split()
    dataType = words[0]
    if dataType == "int":
        info = {}
        left = int(words[1])
        right = int(words[2])
        info["range"] = (left, right)
        cin["int"] = info
    elif dataType == "float":
        info = {}
        left = float(words[1])
        right = float(words[2])
        info["range"] = (left, right)
        cin["float"] = info
    elif dataType == "str":
        info = {"range": words[1], "length": int(words[2])}
        cin["str"] = info
    else:
        continue

print("随机结构: {:}".format(cin))
ans = generateRandom(5, **cin)
for elem in ans:
    print(elem)
