def funcA():
    print("A")


def funcB():
    print("B")


def funcC():
    print("C")


def funcD():
    print("D")


def txtFileReader(file):
    files = []
    with open(file) as f:
        for line in f:
            files.append(line)
    f.close()
    return files


funcs = {"a": funcA, "b": funcB, "c": funcC, "d": funcD, "e": txtFileReader}


def callFuncs(action,file):
    # funcs[action]()
    funcs[action]()
    # with open(file) as f:
    #     for line in f:
    #         print(line)


# callFuncs("b","Test.txt")