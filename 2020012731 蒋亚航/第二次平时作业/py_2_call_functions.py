import py_functionsPackage.py_functions as py_functions


def txtFileReader(file, lstfiles=None):

    with open(file) as f:
        lstfiles = []
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

# 1. load a config txt file, obtaining function name.

funcsname = txtFileReader("functionlist.txt")

# 2. define a function, and use it to call the functions in the package.

def callPackageFunc(funcName: str):
   print(eval(funcName))

# 3. test st.2.
callPackageFunc(funcsname.pop())
