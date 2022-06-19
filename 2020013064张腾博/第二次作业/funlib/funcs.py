def funcA():
    print("funcA")


def funcB():
    print("funcB")


def funcC():
    print("funcC")


def txtFileReader(file):
    listfiles = []
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            listfiles.append(line)
    f.close()
    return listfiles


funcs = {"a": funcA, "b": funcB, "c": funcC}


def callFuncs(action):
    funcs[action]()


# callFuncs("c")
