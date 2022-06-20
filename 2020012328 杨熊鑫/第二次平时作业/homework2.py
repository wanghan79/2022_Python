import string
import myOwnFunction.newFunctions as funcs


# This function handles the external file.
def fileRead(file):
    lines = []
    with open(file, 'r') as f:
        for line in f:
            lines.append(line)
    return lines


if __name__ == '__main__':
    Funcs = fileRead("function_list.txt")
    for func in Funcs:
        eval("funcs." + func)()
