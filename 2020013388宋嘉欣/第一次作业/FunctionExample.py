import random
import string
def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles
def structDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
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
def apply():
    lststruct = txtFileReader("struct.txt")
    for item in lststruct:
        para = eval(item)
        result = structDataSampling(**para)
        for i in result:
            print(i)

apply()



