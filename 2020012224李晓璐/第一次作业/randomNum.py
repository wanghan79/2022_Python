import random
import string
def structDateSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
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

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

def apply():
    #para = {"num":5, "struct": {"int": {"datarange": (0, 10000)}, "double": {"datarange": (0, 10000)},"str": {"datarange": string.ascii_letters, "len": 10}}}
    paradate = txtFileReader("paraDate.txt")
    para = eval(paradate.pop())
    result = structDateSampling(**para)
    for item in result:
        print(item)

apply()
