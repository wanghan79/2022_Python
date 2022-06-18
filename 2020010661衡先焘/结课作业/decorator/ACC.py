"""
   Author: hxt
   Created: 2022/5/26 
"""
import logging

from decorator.BaseCC import BaseCC

logger = logging.getLogger(__name__)


class Decorator(BaseCC):
    def __init__(self, func):
        """
        ACC修饰器
        :param func: 传入函数
        """
        super(Decorator, self).__init__("ACC")
        self._func = func
        self.__name = "ACC"
        self.struct = None
        self.__tp_tn = 0  # 存储所有数据计算结果，以便求总共的acc值
        self.__total_num = 0  # 存储所有数据的组数

    def __call__(self, *args, **kwargs):
        super(Decorator, self).__call__(self._func)
        structTmp = self._func(*args, **kwargs)
        flag = 1
        while True:
            try:
                self.struct = next(structTmp)
                core_value = self.__core__()
                logger.info("第{:}波".format(flag) + "数据 --> Accuracy: {:.2%}".format(core_value))
                flag += 1
            except StopIteration:
                total_core_value = self.__calculate_total__()
                logger.info("所有数据一共有的 --> Accuracy: {:.2%}\n".format(total_core_value))
                break
        # 此外返回与不返回没什么影响
        return structTmp

    def __core__(self):
        """
        计算MCC的核心代码，每一批数据都计算
        """
        data_list = list()
        tp_tn = 0
        for i in self.struct:
            data_list.append(not i[0] ^ i[1])
            if not i[0] ^ i[1]:
                tp_tn += 1
        self.__tp_tn += tp_tn
        self.__total_num += len(self.struct)
        return tp_tn / len(self.struct)

    def __calculate_total__(self):
        """
        用已经计算并存储好的数据，进行总的MCC计算
        """
        return self.__tp_tn / self.__total_num
