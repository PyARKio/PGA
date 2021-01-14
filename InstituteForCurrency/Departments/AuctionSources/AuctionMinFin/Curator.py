# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AuctionSources.AuctionMinFin.AuctionUSD import AuctionUSD
from InstituteForCurrency.Departments.AuctionSources.AuctionMinFin.AuctionEUR import AuctionEUR
from Memento.InstituteForCurrency.Departments.Auction import AuctionCuratorMemento
from Arsenal.Chronicler import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MinFinCurator(AuctionCuratorMemento):
    def __init__(self, chrono):
        log.info('USD: {}'.format(self._get_one_obj({'currency': 'USD'})['minfin_usd']))
        log.info('EUR: {}'.format(self._get_one_obj({'currency': 'EUR'})['minfin_eur']))
        self.__usd = AuctionUSD(source=self._get_one_obj({'currency': 'USD'})['minfin_usd'], chrono=chrono)
        self.__eur = AuctionEUR(source=self._get_one_obj({'currency': 'EUR'})['minfin_eur'], chrono=chrono)
        # self.__pln = AuctionPLN(source=self.get_one_obj({'currency': 'PLN'})['minfin_pln'], chrono=chrono)

        self.__directions = {'USD': self.__usd.appeal,
                             'EUR': self.__eur.appeal,
                             }

    def answer_from_curator(self):
        ...

    def question_to_curator(self, question):
        answer_to_departament = {}
        for key, value in question.items():
            answer_to_departament[key] = self.__directions[key](value)
        return answer_to_departament
