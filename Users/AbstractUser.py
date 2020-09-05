# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from abc import ABC, abstractmethod
from Arsenal.log_settings import log
from Arsenal.url_obj import URL


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractUser(ABC):
    def __init__(self, uid, name):
        self.__id = uid
        self.__name = name
        self.__email = None





