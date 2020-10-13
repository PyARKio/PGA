# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureBank
from Memento.InstituteForCurrency.Sources.Bank import BankEURMemento
from Arsenal.Chronicler import log
from Arsenal.URL_Object import URL
from datetime import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class BankEUR(AbstractSource, BankEURMemento):
    def __init__(self, source, chrono):
        super().__init__()
        self.__chronometer = chrono
        self.__bank_eur = URL(source['EUR'])

        self.__eur = StructureBank(currency='EUR')

        self._report = {'EUR': self.__eur}

        self._get_currency = [self.__get_eur]

        self._add_mark()

    def __get_eur(self):
        if self.__bank_eur.status():
            bid_offer, week = self.__parser(self.__bank_eur.data['content'])

            self.__eur.time = datetime.now()
            self.__eur.bid.main = bid_offer[0]
            self.__eur.bid.diff = bid_offer[1]
            self.__eur.offer.main = bid_offer[3]
            self.__eur.offer.diff = bid_offer[2]
            self.__eur.week = week[0]

            log.info(self.__eur.str)

            self._report['EUR'] = self.__eur

        else:
            for i, v in self.__bank_eur.errors.items():
                log.debug(i)
                log.debug(v)

    def _add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self._set_delay(), 'CallBack': self.check})






