import random

'''
作业要求:
    编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，
    并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数
'''


# 随机数生成
def randomNumberGenerator(**struct):
    result = list()
    for item in range(0, struct['num']):
        element = list()
        # 对每个参数列表的每个键值对
        for key, value in struct.items():
            if key == "num":
                continue
            elif key == "int":
                # 将容器类型或者序列类型的转换为可迭代对象，类似于JAVA中的Iterator迭代器
                it = iter(value['dataRange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['dataRange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                # 'sep'.join(seq)，以sep作为分隔符，将seq所有的元素合并成一个新的字符串
                # 这里分隔符就是没有，会得到连贯的字符串
                # random.choice 从给定的一维数组随机采样
                tmp = ''.join(random.choice(value['dataRange']) for _ in range(value['length']))
            else:
                print("数据错误")
                continue
            element.append(tmp)
        result.append(element)
    return result


# 读取txt文件得到生成随机数所需要的参数，获得参数列表
def readFileToDataStruct(filePath):
    # 打开文件，赋予只读权限（自动关闭文件）
    with open(filePath, "r") as f:
        dataText = f.readlines()
    num = 0
    dataStruct = {}

    for line in dataText:
        words = line.split()
        # 判断第一行取出数据需要的数据条目num
        if words.__len__() == 1:
            num = int(words[0])
            continue
        dataType = words[0]
        dataStruct["num"] = num
        if dataType == "int":
            # 读取的都是字符串，需要强转成所需要的类型
            info = {"dataRange": (int(words[1]), int(words[2]))}
            dataStruct["int"] = info
        elif dataType == "float":
            info = {"dataRange": (float(words[1]), float(words[2]))}
            dataStruct["float"] = info
        elif dataType == "str":
            info = {"dataRange": words[1], "length": int(words[2])}
            dataStruct["str"] = info
        else:
            continue
    return dataStruct


# 本文件运行时执行的代码
if __name__ == "__main__":
    myDataStruct = readFileToDataStruct('DataParam.txt')
    ans = randomNumberGenerator(**myDataStruct)
    print('读取参数：', myDataStruct)
    print("生成数据：↓")
    for elem in ans:
        print(elem)


'''
打印结果样例：
读取参数： {'num': 10, 'int': {'dataRange': (10, 20)}, 'float': {'dataRange': (100.0, 200.0)}, 'str': {'dataRange': 'qwertyuiQWERTYUI!@#$%^&*()', 'length': 10}}
生成数据：↓
[20, 186.25876202213854, ')eWT^qwe#R']
[20, 131.11745979127267, 'Tre#i$QwY*']
[17, 118.31486968046468, 'RTqYu!@Yi%']
[12, 163.92875849310545, 'q@*#uw#Uq@']
[19, 156.79704484687338, 'IqEeWrEYet']
[18, 156.42218322976305, 'TU!@!TQiw@']
[11, 153.33002891733852, 'E#w!R#urUU']
[14, 112.93529807782858, 'rqIuY#^YR#']
[19, 164.05326218599845, 'T(ewQ#Y^)W']
[18, 145.23308279224761, 'w)!R@w$#rt']

Process finished with exit code 0
'''