# 作业1
import random
import string
from unittest import result

# 根据给定字典，生成num个给定数据结构的随机数据，用list表示
def structDataSampling(**Kwargs):
    result=list()
    for item in range(0,Kwargs["num"]):
        element=list()
        for key,value in Kwargs["struct"].items():
            if key=="int":
                it=iter(value["datarange"])
                tmp=random.randint(next(it), next(it))
            elif key=="float":
                it=iter(value['datarange'])
                tmp=random.uniform(next(it),next(it))
            elif key=="str":
                tmp=''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

# 读文件
def txtFileReader(file):
    listfiles = []
    with open(file) as f:
        for line in f:
            listfiles.append(line)
    f.close()
    return listfiles

# para为list
para = txtFileReader("excercise1.txt")
# 字符转换为字典
kpara = eval(para[0])
# 输出
re = structDataSampling(**kpara)
print(re)
