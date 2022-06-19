'''
Created on April 22, 2022
@author: Ivan Li
'''

# import related packages
from funcsPack import callFuncs as funcs

# read the function name specified in the text file
def readFunctions(filePath):
    with open(filePath, 'r') as f:
        funcsName = f.read().split()
    for func in funcsName:
        eval('funcs.' + func)()


if __name__ == '__main__':
    print(__doc__)
    filePath = 'funclist.txt'
    readFunctions(filePath)