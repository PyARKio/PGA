# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from abc import ABC, abstractmethod
from utilits.log_settings import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        log.debug(self)


class MainDiff(object):
    def __init__(self, name):
        self.__name = name
        self.main = None
        self.diff = None

    def __str__(self):
        return '{}.Main: {}; {}.Diff: {}'.format(self.__name, self.main, self.__name, self.diff)






