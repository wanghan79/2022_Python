import random
import string

def structDataSampling(**kwargs):
#**kwargs 关键字参数 本质是dist
    """
    :param num:
    :param struct:
    :return:
    """
    num = kwargs['num']
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


file = open("Para.txt",'r') #读取文件
read_para = file.read()
file.close()
#print(read_para)
para = eval(read_para)
#print(type(para))
print(structDataSampling(**para))
'''

para = {
    "num": 5,
    "struct": {
        "int": {"datarange": (0, 100)},
         "float": {"datarange": (0, 10000)},
        "str": {"datarange": string.ascii_uppercase, "len": 50}
    }
} #字典嵌套字典，字典里字符串：元组

print(para['struct']['int']['datarange'])
print(para["struct"])
print(para['num'])
print(structDataSampling(**para))
'''

