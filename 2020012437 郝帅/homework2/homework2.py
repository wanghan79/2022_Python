import hspackage.functions as hs

def printflist(name:str):
    print(eval(name))

list = []

file = open("hw2.txt",'r')
for i in file:
    list.append(line.strip())
file.close()
for i in list:
    printflist(i)
