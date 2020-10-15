# -- coding: utf-8 --
from __future__ import unicode_literals
from .BankSources.BankMinFin.Curator import MinFinCurator
from .BankSources.BankKurs.Curator import KursCurator
from .BankSources.BankFinance.Curator import FinanceCurator
from Arsenal.Chronicler import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Bank:
    def __init__(self, chrono):
        self.__minfin = MinFinCurator(chrono)
        # self.__kurs = KursCurator(chrono)
        # self.__finance = FinanceCurator(chrono)

    def answer(self):
        ...

    def question(self, question):
        ...
