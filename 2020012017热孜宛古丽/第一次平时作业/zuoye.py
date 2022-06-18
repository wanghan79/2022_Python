import random
def fuc(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(len))

            else:
                break
            element.append(tmp)
        result.append(element)
    return result

with open('test.txt','r',encoding='utf-8') as f:
    dic=[]
    for line in f.readlines():
        line=line.strip('\n') #换行
        a=line.split(',',1)   #以空格为分隔符，分割成两个
        a[1]=eval(a[1])
        dic.append(a)
        struct=dict(dic)

result=fuc(3,**struct)
for item in result:
    print(item)
