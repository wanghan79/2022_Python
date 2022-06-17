"""

"""
import random
import string
def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

def dataSampling(**kwargs):
    '''

    :param kwargs:
    :return:
    '''
    result = list()
    for i in range(0, kwargs['num']):
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

# para = eval(txtFileReader("in.txt").pop())
def apply():
    lststruct = txtFileReader("in.txt")
    for item in lststruct:
        para = eval(item)
        ans = dataSampling(**para)
        for i in ans:
            print(i)

apply()






