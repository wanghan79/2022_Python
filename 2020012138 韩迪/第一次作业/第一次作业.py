# coding=utf-8

import random


def structDataSampling(num, **kwargs):
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
            elif key == 'str':
                tmp = ''
                for i in range(0, value['len']):
                    tmp = tmp + random.SystemRandom().choice(value['datarange'])
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def readFile(filePath):
    rtnLst = []
    with open(filePath, 'r') as fp:
        listX = fp.readlines()
    for n in listX:
        n = ('struct=' + n).strip('\n')
        rtnLst.append(n)
    return rtnLst


struct = {}  # Dummy Variable for Function monkeyPatchMain()


def monkeyPatchMain():
    filePath = input('Input File Path Here: ')
    randTimes = int(input('Input Random Sample Times Here: '))
    getLst = readFile(filePath)
    for n in getLst:
        exec(n, globals())  # Monkey Patch (Hotfix)
        randomResult = structDataSampling(randTimes, **struct)
        for item in randomResult:
            print(item)


try:
    monkeyPatchMain()
except KeyboardInterrupt:
    print('\nExit NOW !!!')
    pass
