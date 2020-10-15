# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.BankSources.BankMinFin.BankUSD import BankUSD
from InstituteForCurrency.Departments.BankSources.BankMinFin.BankEUR import BankEUR
from Memento.InstituteForCurrency.Departments.Bank import BankCuratorMemento


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MinFinCurator(BankCuratorMemento):
    def __init__(self, chrono):
        self.__usd = BankUSD(source=self.get_one_obj({'currency': 'USD'})['minfin_usd'], chrono=chrono)
        self.__eur = BankEUR(source=self.get_one_obj({'currency': 'EUR'})['minfin_eur'], chrono=chrono)
        # self.__pln = BankPLN(source=self.get_one_obj({'currency': 'PLN'})['minfin_pln'], chrono=chrono)

    def answer_from_curator(self):
        ...

    def question_to_curator(self, question):
        ...


if __name__ == '__main__':
    from Arsenal.Chronometer import Chronometer

    chronometer = Chronometer()
    chronometer.start()
    minfin = MinFinCurator(chronometer)
