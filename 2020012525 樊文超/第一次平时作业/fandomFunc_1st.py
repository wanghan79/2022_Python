import random

'''
    平时作业一：
    编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，
    并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数
'''

# 随机数生成
def randomNumberGeneratior(**struct):
    result = list()
    for index in range(0, struct['num']):
        element = list()
        # 获取键--数据类型 值--范围
        for key, value in struct.items():
            if key == "num":
                continue
            elif key == "int":
                it = iter(value['dataRange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['dataRange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.choice(value['dataRange']) for _ in range(value['len']))
            else:
                print('暂不支持该类型')
                break
            element.append(tmp)
        result.append(element)
    return result

# 读取txt文件获取参数
def fileReader(filePath):
    with open(filePath, 'r') as f:
        dataText = f.readlines()
    num = 0
    dataStruct = {}
    for line in dataText:
        words = line.split()
        if words.__len__() == 1:
            num = int(words[0])
            continue
        dataType = words[0]
        dataStruct['num'] = num
        if dataType == 'int':
            rng = {'dataRange': (int(words[1]), int(words[2]))}
            dataStruct['int'] = rng
        elif dataType == 'float':
            rng = {'dataRange': (float(words[1]), float(words[2]))}
            dataStruct['float'] = rng
        elif dataType == 'str':
            rng = {'dataRange': words[1], 'len': int(words[2])}
            dataStruct['str'] = rng
        else:
            continue
    return dataStruct

if __name__ == '__main__':
    dataStruct = fileReader('DataParam.txt')
    data = randomNumberGeneratior(**dataStruct)
    print('读取参数：', dataStruct)
    print('生成数据：')
    for elment in data:
        print(elment)