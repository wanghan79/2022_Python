import random
import string
import json

def structDataSamping(**kwargs):
    result=list()
    for item in (0,kwargs['num']):
        element=list()
        for key,value in kwargs['struct'].items():
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
    f=open('zuoye1.txt','r')
    js=f.read()
    struct=json.loads(js)

    result=structDataSamping(**struct)
    for tmp in result:
        print(tmp)

apply()