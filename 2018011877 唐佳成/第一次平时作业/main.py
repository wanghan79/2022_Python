# 平时作业一：编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数

from ast import parse
from functools import total_ordering
import json
import random
import re

def gen_int(define):
    return random.randint(define[1], define[2])

def gen_float(define):
    return random.random() * ( define[2] - define[1] ) + define[1]

# 支持reg的一个子集，即 (a | [a-z]) ( ? | {n} | {n, m} )?
# parser 会将其分解为一个数组

def reg_parse(reg: str):
    spans = []
    it = 0
    length = len(reg)
    while it < length:
        ch = reg[it]
        span = [ ch, 1, 1 ]
        if ch == "[":
            pos = reg.find("]", it + 1)
            charset = reg[it+1:pos]
            parsed_charset = []
            for group in re.findall(r"(.(-.)?)", charset):
                char = group[0]
                if len(char) == 1:
                    parsed_charset.append(char)
                else:
                    parsed_charset.append((ord(char[0]), ord(char[2])))
            span[0] = parsed_charset
            it = pos + 1
        else:
            it = it + 1
        if it < length and reg[it] == "?":
            it = it + 1
            span[1] = 0
        elif it < length and reg[it] == "{":
            pos = reg.find("}", it + 1)
            param = reg[it+1:pos] 
            tuple = eval("(%s, %s)" % (param, param))
            span[1] = tuple[0]
            span[2] = tuple[1]
            it = pos + 1
        spans.append(span)
    return spans

def gen_str(define):
    res = ""
    reg_spans = reg_parse(define[1])
    for span in reg_spans:
        l = random.randint(span[1], span[2])
        for i in range(l):
            if isinstance(span[0], str):
                res += span[0]
            else:
                total = 0
                for ci in span[0]:
                    if isinstance(ci, str):
                        total += 1
                    else:
                        total += ci[1] - ci[0] + 1
                nw = random.randint(1, total)
                for ci in span[0]:
                    if isinstance(ci, str):
                        nw -= 1
                        if nw == 0:
                            res += nw
                            break
                    else:
                        nw -= ci[1] - ci[0] + 1
                        if nw <= 0:
                            res += chr(ci[1] + nw)
                            break

    return res

def gen_dispatch(define):
    return {
        "int": gen_int,
        "float": gen_float,
        "string": gen_str,
    }[define[0]](define)

def gen_data(**kwargs):
    res = {}
    for name, define in kwargs.items():
        res[name] = gen_dispatch(define)
    return res

with open('./ds.json', 'r', encoding='utf-8') as f:
    define = json.load(f)

for i in range(10):
    data = gen_data(**define)
    print(
        "===========",
        " data #%d " % i,
        "==========="
    )
    print(data)
