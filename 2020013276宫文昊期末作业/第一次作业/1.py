import random
import string


myFile = open('structData.txt','r')
para = eval(myFile.read())
print(para)

def structDataSampling(**kwargs):

    result = list()
    for item in range(0, kwargs['num']):
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



def main():
    result = structDataSampling(**para)
    for item in result:
        print(item)

main()