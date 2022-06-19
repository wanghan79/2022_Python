"""
    Author:  Liu
    Purpose: pass.
    Created: 6/5/2022
"""
import random
import string


def structDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key,value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def txtFileReader(file):
    listfiles = []
    with open(file) as f:
        for line in f:
            listfiles.append(line)
    f.close()
    return listfiles

randomname = txtFileReader("example1.txt")

def callRandom():
    item = eval(randomname.pop())
    result = structDataSampling(**item)
    for i in result:
        print(i)

callRandom()