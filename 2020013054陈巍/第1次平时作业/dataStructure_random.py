import random
def generateStructData(num,**dic):
    '''
    :param num:
    :param kargs:
    :return:  a list of generateing random data for a given number of data structures
    '''
    result=[]
    for i in range(int(num)):
        data = []
        for key,value in dic.items():

            if key=='int':
                data.append(random.randint(value['range_min'],value['range_max']))
            if key=='bool':
                data.append(random.choice((True, False)))
            if key=='float':
                data.append(random.randint(value['range_min'], value['range_max']))
            if key=='string':
                lst=random.sample(value['range'],value['length'])
                data.append(''.join(lst))
        result.append(data)
    return result

with open ("struct.txt",'r',encoding='utf-8')as f:
    struct_data =  f.readlines() #list
    struct_dic ={}
    info ={}
    for line in struct_data:
        a = line.split()
        struct=a[0]
        if struct == 'int':
            info['range_min']=(int(a[1]))
            info['range_max'] = (int(a[2]))
        elif struct == 'bool':
            info = None
        elif struct == 'float':
            info['range_min'] = (int(a[1]))
            info['range_max'] = (int(a[2]))
        elif struct == 'string':
            info['range']=a[1]
            info['length']=int(a[2])
        else:
            print("不支持此类型数据！")
            continue
        struct_dic[struct]=info

num = input("请输入随机数据结构的给定个数：")
print(generateStructData(num,**struct_dic))




