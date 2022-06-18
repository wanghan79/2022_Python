"""
   Author: hxt
   Created: 2022/6/3 
"""
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def generateRandom1(path="../data/test.txt", randomSize=1):
    """
    生成随机结构，全部一次性生成,return
    :param path:
    :param randomSize:
    :return:
    """
    cin = generateStruct(path)
    ans = __generateRandom(randomSize, **cin)
    for n in ans:
        print(n)
    return ans


def generateStruct(path="../data/test.txt"):
    """
    预处理数据，转成**struct
    :param path:  文件路径
    :return: **struct
    """
    with open(path, "r", encoding='utf-8') as f:
        structText = f.readlines()
    cin = {}
    for line in structText:
        if line.startswith("###########"):
            logger.info("读取文件完成")
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
            info = {}
            info["range"] = words[1]
            info["length"] = int(words[2])
            cin["str"] = info
        elif dataType == "tuple":
            info = {}
            infoRange = []
            split = words[1].split("|")
            for i in split: infoRange.append(__tupleGenerate(i))
            info["range"] = infoRange
            info["length"] = int(words[2])
            cin["tuple"] = info
        else:
            continue
    logger.info("随机结构: " + str(cin) + "\n")
    return cin


class GenerateRandom2:
    """
    生成随机结构，用yield依次生成
    :param num: 生产几批数据
    :param struct: 生产的结构
    :return:随机数据集
    """

    def __init__(self, num, **struct):
        self.num = num
        self.struct = struct

    def __iter__(self):
        if self.num <= 0:
            print("num = ", self.num, "num must > 0")
            return
        for i in range(self.num):
            element = list()
            tmp = None
            for key, val in self.struct.items():
                if key == "int":
                    it = iter(val["range"])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(val["range"])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    strRange = val["range"]
                    strLength = val["length"]
                    string = ""
                    tmp = []
                    for j in range(strLength):
                        string += random.choice(strRange)
                    tmp.append(string)
                elif key == "tuple":
                    strRange = val["range"]
                    strLength = val["length"]
                    tupleList = []
                    tmp = list()
                    for j in range(strLength):
                        tupleList.append(random.choice(strRange))
                    tmp.append(tupleList)
                    pass
                else:
                    element.append("未知类型")
            yield tmp


def __tupleGenerate(string):
    """
    将字符串的元组转换成元组
    :param string: 元组字符串
    :return: 元组
    """
    r = string
    temp = r.replace('(', '').replace(')', '')
    a = tuple([int(i) for i in temp.split(',')])
    return a


def __generateRandom(num, **struct):
    """
    一次性生成所有的随机结构
    :param num: 随机个数
    :param struct: 随机结构体
    :return: 数组
    """
    if num <= 0:
        logger.error("num = ", num, "num must > 0")
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
            elif key == "tuple":
                strRange = val["range"]
                strLength = val["length"]
                tupleList = []
                for j in range(strLength):
                    tupleList.append(random.choice(strRange))
                element.append(tupleList)
                pass
            else:
                element.append("未知类型")
        result.append(element)
    return result
