# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.MasterCardSources.MasterCardMinFin.MasterCardUSD import MasterCardUSD
from InstituteForCurrency.Departments.MasterCardSources.MasterCardMinFin.MasterCardEUR import MasterCardEUR
from Memento.InstituteForCurrency.Departments.MasterCard import MasterCardCuratorMemento


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MinFinCurator(MasterCardCuratorMemento):
    def __init__(self, chrono):
        self.__usd = MasterCardUSD(source=self._get_one_obj({'currency': 'USD'})['minfin_usd'], chrono=chrono)
        self.__eur = MasterCardEUR(source=self._get_one_obj({'currency': 'EUR'})['minfin_eur'], chrono=chrono)
        # self.__pln = BankPLN(source=self.get_one_obj({'currency': 'PLN'})['minfin_pln'], chrono=chrono)

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


if __name__ == '__main__':
    from Arsenal.Chronometer import Chronometer

    chronometer = Chronometer()
    chronometer.start()
    minfin = MinFinCurator(chronometer)
