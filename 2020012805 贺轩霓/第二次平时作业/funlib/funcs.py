def funcA():
    print("funcA")


def funcB():
    print("funcB")


def funcC():
    print("funcC")


def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles
