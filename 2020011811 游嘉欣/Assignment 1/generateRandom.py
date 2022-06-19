"""
    Author：Jacy
    Purpose：Pass
    Created:2022/6/16
"""
import random
import string
def generateRandom(**kargs):
    result=list()
    num=kargs["num"]
    struct=kargs["struct"]
    for k in range(num):
        elem=list()
        for key,value in struct.items():
            if key=="int":
                it =iter(value["range"])
                elem.append(random.randint(next(it),next(it)))
            elif key=="float":
                it =iter(value["range"])
                elem.append(random.uniform(next(it),next(it)))
            elif key=="str":
                Range=value["range"]
                Length=value["length"]
                string=""
                for i in range(Length):
                    string+=random.choice(Range)
                elem.append(string)
            else:
                elem.append("未知类型")
        result.append(elem)
    return result
argument ={"num":10."struct":{"int":{"range":(10,20)},"float":{"range":(100,150)},"str":{"range":string.ascii_uppercase,"length":10}}}

with open("Str.txt", "r") as f:
    Text=f.readlines()
num=int(Text[0].split()[0])
cin = {}
cin["num"]=num
struct={}
for line in Text:
    words=line.split()
    dataType==words[0]
    if dataType=="int":
        info={}
        left=int(words[1])
        right=int(words[2])
        info["range"]=(left,right)
        struct["int"]=info
    elif dataType=="float":
        info={}
        left = float(words[1])
        right = float(words[2])
        info["range"] = (left, right)
        struct["float"] = info
    elif dataType=="str":
        info={}
        info["range"]=words[1]
        info["length"]=int(wores[2])
        struct["str"]=info
    else:
        continue
cin["strcut"]=strcut
ans=generateRandom(**cin)
for element in ans:
    print(element)
