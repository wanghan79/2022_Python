"""
   Author: hxt
   Created: 2022/5/26 
"""

class Decorator:
    def __init__(self, func):
        self._func = func
        self.struct = None

    def __call__(self, *args, **kwargs):
        self.struct = self._func(*args, **kwargs)
        core_value = self.__core__()
        print("Accuracy: {:.2%}".format(core_value))
        # 仍然返回传入的struct，以便结构体再次被其他修饰器修饰。
        return self.struct

    def __core__(self):
        data_list = list()
        tp_tn = 0
        for i in self.struct:
            data_list.append(not i[0] ^ i[1])
            if not i[0] ^ i[1]:
                tp_tn += 1
        return tp_tn / len(self.struct)
