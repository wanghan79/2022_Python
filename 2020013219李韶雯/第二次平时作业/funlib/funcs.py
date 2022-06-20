def funca():
    print("这里是funcA")


def funcb():
    print("这里是funcB")


def funcc():
    print("这里是funcC")


def funcd():
    print("这里是funcD")


def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles


