# -- coding: utf-8 --
from __future__ import unicode_literals
from .AuctionSources.AuctionMinFin.Curator import MinFinCurator
# from .AuctionSources.AuctionKurs.Curator import KursCurator
# from .AuctionSources.AuctionFinance.Curator import FinanceCurator
from Arsenal.Chronicler import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Auction:
    def __init__(self, chrono):
        self.__minfin = MinFinCurator(chrono)
        # self.__kurs = KursCurator(chrono)
        # self.__finance = FinanceCurator(chrono)

    def answer(self):
        ...

    def question(self, question):
        ...

