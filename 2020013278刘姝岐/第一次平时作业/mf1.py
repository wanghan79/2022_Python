#读入
with open('list.txt', encoding='utf8') as f:
    name = f.readline().strip().split(',')  # 读取文件第一行转成list，作为字典的key
    fruit_list = []
    for line in f:  # 用for循环遍历句柄f，优点是无论文件有多大，读取都不会撑爆内存。
        # 不要用read()或readlines()，万一处理的文件超大会导致撑爆内存。
        if len(line) < 3:  # 过滤空行及数据不完整的行。
            continue
        line = line.strip().split(',')  # 将文件内容按','分隔转成列表
        fruit_dict = {}  # 声明一空字典，保存每一行的内容
        for i in range(len(name)):  # 通过下标遍历name列表
            fruit_dict[name[i]] = line[i]
        #fruit_list.append(fruit_dict)
    print(fruit_dict)

 #关键字参数
def fruit(name, price, **kw):
    print('name:', name, 'price:', price, 'other:', kw)

fruit('apple', 4.8, number=5)

extra={'number':5}
fruit('apple', 4.8, **extra)
