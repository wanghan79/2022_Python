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
        self.__tp = 0  # 存储MCC计算过程中的数据
        self.__tn = 0  # 因为每一次遍历都会消耗内存，用完这一批就丢掉了
        self.__fp = 0  # 在每次遍历的过程中存储下这些数据，可以大大减少内存消耗
        self.__fn = 0  # 从而提高程序效率，增加数据的可操作的上限

    def __call__(self, *args, **kwargs):
        super(Decorator, self).__call__(self._func)
        structTmp = self._func(*args, **kwargs)
        flag = 1
        while True:
            try:
                self.struct = next(structTmp)
                core_value = self.__core__()
                logger.info("第{:}波".format(flag) + "数据 --> MCC: {:.2%}".format(core_value))
                flag += 1
            except StopIteration:
                total_core_value = self.__calculate_total__()
                logger.info("所有数据一共有的 --> MCC: {:.2%}\n".format(total_core_value))
                break
        # 此外返回与不返回没什么影响
        return structTmp

    def __core__(self):
        """
        计算MCC的核心代码，每一批数据都计算
        """
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
        self.__tp += tp
        self.__tn += tn
        self.__fp += fp
        self.__fn += fn
        return (tp * tn - fp * fn) / \
               math.sqrt((tp + fp) * (fn + tp) * (fn + tn) * (fp + tn))

    def __calculate_total__(self):
        """
        用已经计算并存储好的数据，进行总的MCC计算
        """
        return (self.__tp * self.__tn - self.__fp * self.__fn) / \
               math.sqrt((self.__tp + self.__fp) *
                         (self.__fn + self.__tp) *
                         (self.__fn + self.__tn) * (self.__fp + self.__tn))
