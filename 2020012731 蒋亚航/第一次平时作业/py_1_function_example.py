import random
import string


def structDataSampling(num, **kwargs):


    result = list
    for index in range(0, num):
        element = list
        for key, value in kwargs.items():
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

def txtFileReader(file, lstfiles=None):

    with open(file) as f:
        lstfiles = []
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

list = txtFileReader("keywords.txt")
struct = eval(list[0])



def apply():


    result = structDataSampling(2, **struct)
    for item in result:
        print(item)

apply()