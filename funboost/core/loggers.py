import nb_log

# noinspection PyUnresolvedReferences
from nb_log import get_logger, LoggerLevelSetterMixin, nb_log_config_default
import logging

LOG_FILE_NAME = 'funboost.log'


def get_funboost_file_logger(name, *, log_level_int: int = None, **kwargs):
    """日志自动写入 funboost.log文件中,不需要亲自指定文件名"""
    kwargs['log_filename'] = LOG_FILE_NAME
    return nb_log.get_logger(name, log_level_int=log_level_int, **kwargs, )


class FunboostFileLoggerMixin(nb_log.LoggerMixin):
    """给对象添加一个logger树形,命名空间是类本身,写入funboost.log"""
    subclass_logger_dict = {}

    @property
    def logger(self):
        logger_name_key = self.logger_full_name + '3'
        if logger_name_key not in self.subclass_logger_dict:
            logger_var = get_funboost_file_logger(self.logger_full_name)
            self.subclass_logger_dict[logger_name_key] = logger_var
            return logger_var
        else:
            return self.subclass_logger_dict[logger_name_key]


class MetaTypeFileLogger(type):
    """
    给类添加一个属性.名空间是类本身,写入funboost.log
    """

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.logger = get_funboost_file_logger(name)


flogger = get_funboost_file_logger('funboost', )

# 开发时候的调试日志，比print方便通过级别一键屏蔽。
develop_logger = get_logger('funboost_develop', log_level_int=logging.WARNING, log_filename='funboost_develop.log')

if __name__ == '__main__':
    logger1 = get_funboost_file_logger('name1')
    logger1.info('啦啦啦啦啦啦啦')