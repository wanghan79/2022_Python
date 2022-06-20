import random
import string


def structDataSampling(**kwargs):
    """

    :param num: 生成随机数的个数
    :param kwargs: 字典类型的结构体
    :return: 随机生成的结构
    """
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key,value in kwargs["struct"].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else :
                break
            element.append(tmp)
        result.append(element)
    return result


def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles



def apply():
    struct = txtFileReader('data.txt')
    # print(struct)
    # struct = {"int": {"datarange": (0,10)},
    #           "str": {"datarange":string.ascii_letters,"len": 8}}
    # result = structDataSampling(2,**struct)
    # for item in result:
    #     print(item)
    for item in struct:
        # print(item)
        user_dict = eval(item)
        # print(user_dict)
        result = structDataSampling(**user_dict)
        print(result)



apply()

