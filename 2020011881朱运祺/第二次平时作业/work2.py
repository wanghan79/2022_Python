from funs import myfuns

if __name__ == '__main__':
    with open("funsname.txt", encoding='utf-8') as f:
        for i in f.read().split():
            eval('myfuns.' + i)()
