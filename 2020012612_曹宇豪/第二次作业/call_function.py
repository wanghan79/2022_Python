import func_package.func as funcs


def txtfilereader(file):
    listfile = []
    with open(file) as f:
        for line in f:
            listfile.append(line)
        f.close()
        return listfile


#  step1:read a config txt file,obtaining function name
funcname = txtfilereader('funclist.txt')


#  step2:define a function to call the function in the package
def CallPackage(func_name):
    for i in func_name:
        eval(i)
    # 方法没有return值，会固定return None


#  step3:test the function defined in step2
CallPackage(funcname)
