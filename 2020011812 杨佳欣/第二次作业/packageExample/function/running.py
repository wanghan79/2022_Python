from packageExample.funlib.func import *
a=open("second.txt")
str=a.readlines()
for i in str:
    eval(i.strip('\n'))
a.close()


