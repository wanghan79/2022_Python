import random
import string

def StructDataSampling(**kwargs):
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
            elif key == 'bool':
                cnt = value['count']
                for i in range(cnt):
                    tmp = random.randint(0, 1)
                    element.append(tmp)
            else:
                print("No!!!!! WrongData")
                break
            element.append(tmp)
        result.append(element)
    return result


def apply():
    MyStruct = open("MyStruct.txt")
    para = eval(MyStruct.read()) # 好好记住eval的用法
    result = StructDataSampling(**para)
    for item in result:
        print(item)
    print("完成工作啦awa，请为我的服务打分")

apply()

'''
打印结果样例：
[70, 3858.7561289593864, 'JGFRJTUBZF']
[28, 6932.1296520102105, 'OTKGUUQNNV']
[77, 8010.408260164643, 'ALHZWCPXLQ']
[70, 1140.4038306366037, 'YMLGTYSHGQ']
[19, 8018.023496598435, 'DYXRCINWTO']
'''