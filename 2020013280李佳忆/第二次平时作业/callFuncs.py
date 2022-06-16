"""
Author:KC
Purpose:pass.
Created:{DATE}
"""

import AnotherPackage.funcs as funcs
def txtFileReader(file):
    lstfile = []
    with open(file) as f:
        for line in f:
            lstfile.append(line)
        f.close()
        return lstfile
#STEP 1:read the funclist txt file,obtaining function name
funcname = txtFileReader("funclist.txt")

#STEP 2:define a function to call the functions in the package
def callPackageFunc(funcname):
    for funs in funcname:
        eval(funs)

#STEP 3:test the function defined in STEP2
callPackageFunc(funcname)
