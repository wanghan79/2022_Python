"""
   Author: hxt
   Created: 2022/6/3 
"""
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class BaseCC:

    def __init__(self, name):
        self.__name = name
        pass

    def __call__(self, func):
        logger.info('the function {func} () is running...'.format(func=func.__name__))
        # TODO 这里还可以对下层修饰器做集中的处理，做一些公共的处理，让继承者专注于业务代码
        logger.info("修饰器{:}执行".format(self.__name))

        pass
