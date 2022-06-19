"""
  Author: Wenqian Chen
  Purpose:pass.
  Created:{Date}
"""
import random
import string


def structDataSampling(num, **kwargs):
    """
    :param num:
    :param kwargs:
    :return:
    """
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['strlen']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result




def apply():
    file = open("datastruct.txt")
    stuct = eval(file.read())
    result = structDataSampling(3,**stuct)
    for item in result:
        print(item)

apply()
