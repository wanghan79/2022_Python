import random


def textFileReader(file):
    listfile = []
    with open(file) as f:
        for line in f:
            listfile.append(line)
    f.close()
    return listfile


def kwargsDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
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
        result.append(element)
    return result


def apply():
    data = textFileReader("first.txt")
    keywords = eval(data.pop())
    result = kwargsDataSampling(**keywords)
    for item in result:
        print(item)


apply()
