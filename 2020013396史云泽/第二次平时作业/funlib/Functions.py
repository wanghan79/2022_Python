def funcA():
    print("This is funcA")
    return funcB()

def funcB():
    print("This is funcB")
    return funcC()

def funcC():
    print("This is funcC")
    return funcD()

def funcD():
    print("This is funcD")
    return "Stop!"

def txtFileReader(file):
    lstfiles = []
    with open(file)as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles