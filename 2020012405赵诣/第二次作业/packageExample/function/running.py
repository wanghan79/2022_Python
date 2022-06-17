from packageExample.funlib.func import *
a=open("zhutouhandi.txt")
#单行
# str=a.readline()
# eval(str+"()")

#多行
str=a.readlines()
for i in str:
    eval(i.strip('\n'))
a.close()


