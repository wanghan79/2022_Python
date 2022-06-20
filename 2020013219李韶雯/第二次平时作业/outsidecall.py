import funlib.funcs as funcs


def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles


func = txtFileReader("./config.txt")
# print(func)


def evaloutsidecall(funcNames):
    for item in funcNames:
        eval(item)


evaloutsidecall(func)

