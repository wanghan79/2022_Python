import math
import logging

from decorator.Logger import Logger

logger = logging.getLogger(__name__)


class Decorator(Logger):
    def __init__(self, func):
        super(Decorator, self).__init__("MCC")
        self._func = func
        self.__name = "MCC"
        self.struct = None
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
                core_value = self.__core__()
                logger.info("Case{:}".format(flag) + " --> MCC: {:.2%}".format(core_value))
                flag += 1
            except StopIteration:
                total_core_value = (self.__tp * self.__tn - self.__fp * self.__fn) / math.sqrt(
                    (self.__tp + self.__fp) * (self.__fn + self.__tp) * (self.__fn + self.__tn) * (
                                self.__fp + self.__tn))
                logger.info("Average --> MCC: {:.2%}\n".format(total_core_value))
                break
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
        self.__tp += tp
        self.__tn += tn
        self.__fp += fp
        self.__fn += fn
        return (tp * tn - fp * fn) / math.sqrt((tp + fp) * (fn + tp) * (fn + tn) * (fp + tn))
