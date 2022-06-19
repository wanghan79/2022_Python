"""
   Author: hxt
   Created: 2022/6/10 
"""
import math
import logging

from decorator.BaseCC import BaseCC

logger = logging.getLogger(__name__)


class Decorator(BaseCC):
    def __init__(self, func):
        """
        ACC+MCC修饰器
        具体细节也可以参考看ACC，MCC
        :param func: 传入函数
        """
        super(Decorator, self).__init__("CC")
        self._func = func
        self.__name = "CC"
        self.struct = None
        self.__tp_tn = 0  # 存储所有数据计算结果，以便求总共的acc值
        self.__total_num = 0  # 存储所有数据的组数
        self.__tp = 0
        self.__tn = 0
        self.__fp = 0
        self.__fn = 0

    def __call__(self, *args, **kwargs):
        super(Decorator, self).__call__(self._func)
        structTmp = self._func(*args, **kwargs)
        flag = 1
        while True:
            try:
                self.struct = next(structTmp)
                core_acc_value = self.__core_acc__()
                core_mcc__value = self.__core_mcc__()
                logger.info("第{:}波".format(flag) + "数据 --> ACC: {:.2%}".format(core_acc_value))
                logger.info("第{:}波".format(flag) + "数据 --> MCC: {:.2%}".format(core_mcc__value))
                flag += 1
            except StopIteration:
                total_core_acc_value = self.__calculate_total_acc_()
                total_core_mcc_value = self.__calculate_total_mcc__()
                logger.info("所有数据一共有的 --> ACC: {:.2%}".format(total_core_acc_value))
                logger.info("所有数据一共有的 --> MCC: {:.2%}\n".format(total_core_mcc_value))
                break
        # 此外返回与不返回没什么影响
        return structTmp

    def __core_acc__(self):
        data_list = list()
        tp_tn = 0
        for i in self.struct:
            data_list.append(not i[0] ^ i[1])
            if not i[0] ^ i[1]:
                tp_tn += 1
        self.__tp_tn += tp_tn
        self.__total_num += len(self.struct)
        return tp_tn / len(self.struct)

    def __core_mcc__(self):
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

    def __calculate_total_acc_(self):
        return self.__tp_tn / self.__total_num

    def __calculate_total_mcc__(self):
        return (self.__tp * self.__tn - self.__fp * self.__fn) / \
               math.sqrt((self.__tp + self.__fp) *
                         (self.__fn + self.__tp) *
                         (self.__fn + self.__tn) * (self.__fp + self.__tn))
