# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from abc import ABC, abstractmethod
from utilits.log_settings import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Currency(ABC):
    def __init__(self):
        

    @abstractmethod
    def get_data(self):
        log.debug(self)



