# 平时作业二：编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。

from cmath import exp
from inspect import getmembers
import json
from typing import Any
import jisp.lib

lib = dict(getmembers(jisp.lib))

# 丐版 lisp
# 精神上同 lisp，为了复用json parser，使用中括号代替小括号，除数字以外的token需要写成字符串形式，字符串字面量为以\r开头的字符串
# 宏只支持 defun let cond 三个

INNER_MACROS = [ "defun", "let", "cond" ]

class Context:

     parent: Any

     funcs = {}
     variables = {}

     def __init__(self, parent = None) -> None:
          self.parent = parent

     def defun(self, expr):
          paramList = expr[2]
          def func(*param):
               funcctx = Context(self)
               for i in range(len(paramList)):
                    funcctx.variables[paramList[i]] = param[i]
               value = None
               for subexpr in expr[2:]:
                    value = funcctx.exec(subexpr)
               return value
          self.funcs[expr[1]] = func
          return func

     def let(self, expr):
          value = None
          for decl in expr[1]:
               value = self.variables[decl[0]] = self.cal(decl[1])
          return value

     def cond(self, expr):
          for brench in expr[1:]:
               if self.cal(brench[0]):
                    return self.cal(brench[1])
          return None

     def call(self, func, expr):
          paramValue = []
          for param in expr[1:]:
               paramValue.append(self.cal(param))
          return func(*paramValue)

     def cal(self, expr):
          childctx = Context(self)
          return childctx.exec(expr)

     def findSymbol(self, identifier):
          if not isinstance(identifier, str):
               return ( "value", identifier )
          if identifier[0] == "\r":
               return ( "value", identifier[1:] )
          if identifier in self.funcs:
               return ( "func", self.funcs[identifier] )
          if identifier in self.variables:
               return ( "value", self.variables[identifier] )
          if identifier == "t":
               return ( "value", True )
          if identifier in INNER_MACROS:
               return ( "macro", identifier )
          if self.parent:
               return self.parent.findSymbol(identifier)
          else:
               if identifier in lib:
                    return ( "func", lib[identifier] )
               print("missing symbol: %s" % identifier)
               assert False

     def exec(self, expr):
          if not isinstance(expr, list):
               return self.findSymbol(expr)[1]
          type, value = self.findSymbol(expr[0])
          if type == "macro":
               return getattr(self, value)(expr)
          elif type == "func":
               return self.call(value, expr)
          else:
               return value

def eval_jisp(program):
     ctx = Context()
     for expr in program:
          ctx.exec(expr)


with open('./gcd.jisp', 'r', encoding='utf-8') as f:
     program = json.load(f)

eval_jisp(program)
