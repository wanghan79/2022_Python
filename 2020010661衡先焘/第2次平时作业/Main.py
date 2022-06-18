print("===第2次平时作业===")

def textFileReader():
    linelist = list()
    t = open("data/func.txt")
    for i in t:
        linelist.append(i)
    # read = t.read(10)
    print("读取文件完成")
    t.close()
    return linelist


def callMyFunc(funcName):
    for i in funcName:
        eval(i)


import func.MyFunc as myFunc

reader = textFileReader()
callMyFunc(reader)
