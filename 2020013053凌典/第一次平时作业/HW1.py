import random
import string

"""
作业要求
编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数
"""


def generateRandomData(**kwargs):
    """
    随机数据生成
    :param kwargs: 参数列表
    :return: 对应数据结构的随机数据
    """
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs.items():
            if key == "num":
                continue
            if key == "int":
                it = iter(value["range"])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value["range"])
                tmp = random.uniform(next(it), next(it))
            elif key == "string":
                tmp = ''.join(random.SystemRandom().choice(value["range"]) for _ in range(value["len"]))
            else:
                print("Usage: Data Error!")
                break
            element.append(tmp)
        result.append(element)
    return result


def txtFileToDataStrcut(filename):
    """
    读取txt文件中的信息，生成制定数据结构与其范围所组成的字典
    :param filename: 文件名
    :return: 数据结构与其范围所组成的字典
    """
    with open(filename, "r") as f:
        content = f.readlines()
    ret = {}
    num = 0
    for line in content:
        word = line.split()
        if len(word) == 1:
            num = int(word[0])
            ret["num"] = num
            continue
        type = word[0]
        if type == "int":
            ret[type] = {"range": (int(word[1]), int(word[2]))}
        elif type == "float":
            ret[type] = {"range": (float(word[1]), float(word[2]))}
        elif type == "string":
            ret[type] = {"range": word[1], "len": int(word[2])}
        else:
            print("Usage: Type Error!")
            continue
    return ret


if __name__ == "__main__":
    filename = "data.txt"
    kwargs = txtFileToDataStrcut(filename)
    ret = generateRandomData(**kwargs)
    print("Param: ", kwargs)
    print("Result: ")
    for res_i in ret:
        print(res_i)
