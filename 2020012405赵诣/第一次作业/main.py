#the first homework
import string
import random
def structDataSampling(**kwargs):
    """
    :param num:生成元组个数
    :param kwargs:传入的字典
    :return:各元组生成的各种随机数
    """
    num=kwargs["num"]
    result = list()
    for index in range(0,num):
        element=list()
        for key,value in kwargs['struct'].items():
            if key == "int":
                it=iter(value['datarange'])
                tmp=random.randint(next(it),next(it))
            elif key == "float":
                it=iter(value['datarange'])
                tmp=random.uniform(next(it),next(it))
            elif key == "str":
                it=iter(value['datarange'])
                tmp=''.join(random.sample(value['datarange'], value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result
a=open("handizhu.txt")
parm=eval(a.read())
result=structDataSampling(**parm)
for item in result:
    print(item)
a.close()
