import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


class Logger:

    def __init__(self, name):
        self.__name = name
        pass

    def __call__(self, func):
        logger.info('>>> {func}() execute <<<\n'.format(func=func.__name__))
        pass
