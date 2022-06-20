import string
import random

def structDataSampling(**kwargs):
    try:
        result = list()
        for item in range(0,kwargs['num']):
            element = list()
            for key,value in kwargs['struct'].items():
                if key == "int":
                    # 元组内不是2个数，报错
                    if len(value['datarange']) != 2:
                        raise Exception("datarange must have 2 numbers!")
                    # 元组内2个数相隔太近，无法随机出那么多的数，报错
                    if value['datarange'][1]-value['datarange'][0] < kwargs['num']:
                        raise Exception("The range is too small!")
                    else:
                        it = iter(value['datarange'])
                        tmp = random.randint(next(it), next(it))
                elif key == "float":
                    # 元组内不是2个数，报错
                    if len(value['datarange']) != 2:
                        raise Exception("datarange must have 2 numbers!")
                    # 元组内上界小，下界大，报错
                    if value['datarange'][1] - value['datarange'][0] <= 0:
                        raise Exception("The upper bound is smaller than the lower bound!")
                    else:
                        it = iter(value['datarange'])
                        tmp = random.uniform(next(it),next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result
    except TypeError:
        print("The type is error.")
    except MemoryError:
        print("The memory is error.")
    except ValueError:
        print("The value is error.")
    except Exception as e:
        print(e)

def apply():
    exfile = open("data.txt")
    para = eval(exfile.read())
    result = structDataSampling(**para)
    for item in result:
        print(item)

apply()