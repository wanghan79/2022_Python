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

    def __call__(self, *args, **kwargs):
        super(Decorator, self).__call__(self._func)
        structTmp = self._func(*args, **kwargs)
        flag = 1
        while True:
            try:
                self.struct = next(structTmp)
                core_value = self.__core__()
                logger.info("第{:}波".format(flag) + "数据,Accuracy: {:.2%}".format(core_value))
                flag += 1
            except StopIteration:
                break
        # 此外返回与不返回没什么影响
        return structTmp

    def __core__(self):
        data_list = list()
        tp_tn = 0
        for i in self.struct:
            data_list.append(not i[0] ^ i[1])
            if not i[0] ^ i[1]:
                tp_tn += 1
        return tp_tn / len(self.struct)
