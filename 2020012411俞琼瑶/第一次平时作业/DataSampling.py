"""
    Author: yqy
    Created: 2022/4/24 23:55
"""
import random
import string

# 读取文件，放入字典中
fr = open("para.txt", "r")
para = eval(fr.read())
fr.close()


def structData(**kwargs):
    # result:放置生成的全部数据结构
    result = list()
    for index in range(0, kwargs['num']):
        # element:放置生成的单个数据结构
        element = list()
        for key, value in kwargs['struct'].items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        # 单个数据结构输出
        print(element)
        result.append(element)
    return result


# 调用函数,全部的数据结构输出
print(structData(**para))
