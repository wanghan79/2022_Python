from funcsPack import func


def callFuncFromFile(file):
    funcs = []
    with open(file, 'r') as f:
        for line in f:
            funcs.append(line.strip())

    # call
    for fun in funcs:
        try:
            print("#RUN " + fun + ": ")
            eval('func.' + fun)()
        except AttributeError:
            print("#ERROR: 'funcsPack.func' has no attribute '" + fun + "'")


callFuncFromFile('funclist.txt')

