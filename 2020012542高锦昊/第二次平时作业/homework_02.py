from funs import myfuns

with open("funcsname.txt") as file:
    for funcName in file.read().split():
        eval('myfuns.' + funcName)()
