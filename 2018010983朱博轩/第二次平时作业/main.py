from inspect import getmembers, isfunction

import funlib.funtcions as functions

funcs = dict(getmembers(functions, isfunction))


def reader(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()


def call(funcName, *funcArgs):
    if funcName in funcs:
        return funcs[funcName](*funcArgs)
    else:
        print('Error - function not found')


def call_eval(funcNmae, *funcArgs):
    try:
        return eval(f'functions.{funcNmae}(*funcArgs)')
    except AttributeError:
        print('Error - function not found')


if __name__ == '__main__':
    ls = reader('run.txt')

    for l in ls:
        name, _, args = l.partition('|')
        name = name.strip()
        args = [arg.strip() for arg in args.split('|')]
        args = [arg for arg in args if arg]
        call(name, *args)

    print('-' * 20)

    for l in ls:
        name, _, args = l.partition('|')
        name = name.strip()
        args = [arg.strip() for arg in args.split('|')]
        args = [arg for arg in args if arg]
        call_eval(name, *args)
