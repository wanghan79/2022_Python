"""
   Author: hxt
   Created: 2022/5/26 
"""
import math
import logging

from decorator.BaseCC import BaseCC

logger = logging.getLogger(__name__)


class Decorator(BaseCC):
    def __init__(self, func):
        """
        MCC修饰器
        :param func: 传入函数
        """
        super(Decorator, self).__init__("MCC")
        self._func = func
        self.__name = "MCC"
        self.struct = None

    def __call__(self, *args, **kwargs):
        super(Decorator, self).__call__(self._func)
        structTmp = self._func(*args, **kwargs)
        flag = 1
        while True:
            try:
                self.struct = next(structTmp)
                core_value = self.__core__()
                logger.info("第{:}波".format(flag) + "数据,MCC: {:.2%}".format(core_value))
                flag += 1
            except StopIteration:
                break
        # 此外返回与不返回没什么影响
        return structTmp

    def __core__(self):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for i in self.struct:
            if i[0] & i[1]:
                tp += 1
            elif (~ i[0]) & i[1]:
                fp += 1
            elif i[0] & ~i[1]:
                fn += 1
            else:
                tn += 1
        return (tp * tn - fp * fn) / \
               math.sqrt((tp + fp) * (fn + tp) * (fn + tn) * (fp + tn))
