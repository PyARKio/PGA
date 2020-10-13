# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AuctionDepartment import Auction
from InstituteForCurrency.Departments.BankDepartment import Bank
from InstituteForCurrency.Departments.InterBankDepartment import InterBank
from InstituteForCurrency.Departments.NBUCurrencyDepartment import NBU
from InstituteForCurrency.Departments.MasterCardDepartment import MasterCard
from InstituteForCurrency.Departments.VisaDepartment import Visa
from Arsenal.Chronometer import Chronometer


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Runner(object):
    def __init__(self):
        self.__chronometer = Chronometer()
        self.__chronometer.start()

        self.__auction = Auction(source={'USD': 'https://minfin.com.ua/ua/currency/usd/',
                                         'EUR': 'https://minfin.com.ua/ua/currency/eur/'},
                                 chrono=self.__chronometer)

        self.__bank = Bank(source={'USD': 'https://minfin.com.ua/ua/currency/banks/usd/',
                                   'EUR': 'https://minfin.com.ua/ua/currency/banks/eur/'},
                           chrono=self.__chronometer)

        self.__inter_bank = InterBank(source={'USD': 'https://minfin.com.ua/ua/currency/mb/',
                                              'EUR': 'https://minfin.com.ua/ua/currency/mb/eur/'},
                                      chrono=self.__chronometer)

        self.__nbu = NBU(source={'USD': 'https://minfin.com.ua/ua/currency/nbu/usd/',
                                 'EUR': 'https://minfin.com.ua/ua/currency/nbu/eur/'},
                         chrono=self.__chronometer)

        self.__visa = Visa(source={'USD': 'https://minfin.com.ua/ua/currency/visa/usd/',
                                   'EUR': 'https://minfin.com.ua/ua/currency/visa/eur/'},
                           chrono=self.__chronometer)

        self.__mastercard = MasterCard(source={'USD': 'https://minfin.com.ua/ua/currency/mastercard/usd/',
                                               'EUR': 'https://minfin.com.ua/ua/currency/mastercard/eur/'},
                                       chrono=self.__chronometer)


class PressCentre(Runner):
    def __init__(self):
        super().__init__()

    def appeal(self, letter):
        pass


if __name__ == '__main__':
    press = PressCentre()



