import random
import string

def Node(**text):
    num = test['num']
    ans = list()
    for i in range(0,num):
        res = list()
        for j,k in test['txt'].items():
            if j == 'int':
                t = iter(k['Data'])
                tmp = random.randint(next(t),next(t))
            elif j == 'float':
                t = iter(k['Data'])
                tmp = random.uniform(next(t),next(t))
            elif j == 'str':
                tmp = ''.join(random.SystemRandom().choice(k['Data']) for _ in range(value['cnt'])))
            else:
                break
            res.append(tmp)
        ans.append(res)
    return ans

file = open("hw1.txt",'r')
rf = file.read()
file.close()
f = eval(rf)
printf(Node(**f))
