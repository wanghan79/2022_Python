"""
   Author: hxt
   Created: 2022/5/26 
"""
import math

class Decorator:
    def __init__(self, func):
        super(Decorator, self).__init__()
        self._func = func
        self.struct = None

    def __call__(self, *args, **kwargs):
        self.struct = self._func(*args, **kwargs)
        core_value = self.__core__()
        print("MCC: {:.2%}".format(core_value))
        # 仍然返回传入的struct，以便结构体再次被其他修饰器修饰。
        return self.struct

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
