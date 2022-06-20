import logging

from decorator.Logger import Logger

logger = logging.getLogger(__name__)


class Decorator(Logger):
    def __init__(self, func):
        super(Decorator, self).__init__("ACC")
        self._func = func
        self.__name = "ACC"
        self.struct = None
        self.__tp_tn = 0
        self.__total_num = 0

    def __call__(self, *args, **kwargs):
        super(Decorator, self).__call__(self._func)
        structTmp = self._func(*args, **kwargs)
        flag = 1
        while True:
            try:
                self.struct = next(structTmp)
                core_value = self.__core__()
                logger.info("Case{:}".format(flag) + " --> ACC: {:.2%}".format(core_value))
                flag += 1
            except StopIteration:
                total_core_value = self.__tp_tn / self.__total_num
                logger.info("Average --> ACC: {:.2%}\n".format(total_core_value))
                break
        return structTmp

    def __core__(self):
        data_list = list()
        tp_tn = 0
        for i in self.struct:
            data_list.append(not i[0] ^ i[1])
            if not i[0] ^ i[1]:
                tp_tn += 1
        self.__tp_tn += tp_tn
        self.__total_num += len(self.struct)
        return tp_tn / len(self.struct)
