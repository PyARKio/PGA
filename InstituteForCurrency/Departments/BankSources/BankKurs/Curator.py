# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.BankSources.BankKurs.BankUSD import BankUSD
from InstituteForCurrency.Departments.BankSources.BankKurs.BankEUR import BankEUR
from Memento.InstituteForCurrency.Departments.Bank import BankCuratorMemento


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class KursCurator(BankCuratorMemento):
    def __init__(self, chrono):
        # self.delete_all_obj()
        # self.insert_obj({'currency': 'USD', 'minfin_usd': 'https://minfin.com.ua/ua/currency/banks/usd/'})
        # self.insert_obj({'currency': 'EUR', 'minfin_eur': 'https://minfin.com.ua/ua/currency/banks/eur/'})
        # log.info(self.get_one_obj({'currency': 'USD'}))
        # log.info(self.get_one_obj({'currency': 'EUR'}))
        # log.info(self.get_all_objects())

        self.__usd = BankUSD(source=self.get_one_obj({'currency': 'USD'})['minfin_usd'], chrono=chrono)
        self.__eur = BankEUR(source=self.get_one_obj({'currency': 'EUR'})['minfin_eur'], chrono=chrono)
        # self.__pln = BankPLN(source='', chrono=chrono)

    def answer_from_curator(self):
        ...

    def question_to_curator(self, question):
        ...


if __name__ == '__main__':
    from Arsenal.Chronometer import Chronometer

    chronometer = Chronometer()
    chronometer.start()
    minfin = KursCurator(chronometer)
