import random
import string


def structDataSampling(num, *args, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(num))
            elif key == "bool":
                tmp = list()
                for i in range(0, 2):
                    it = iter(value['datarange'])
                    tmp1 = bool(random.randint(next(it), next(it)))
                    tmp.append(tmp1)
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


# 读取字符串格式的字典返回结果为字典
def txtFileReader(file):
    fr = open(file, 'r+')
    dic = eval(fr.read())  # 读取的str转换为字典
    fr.close()
    return dic


def apply(num):
    struct = txtFileReader("struct")
    result = structDataSampling(num, **struct)
    for item in result:
        print(item)


apply(2)
