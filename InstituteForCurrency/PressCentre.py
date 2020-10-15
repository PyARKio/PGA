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

        self.__auction = Auction(chrono=self.__chronometer)
        self.__bank = Bank(chrono=self.__chronometer)
        self.__inter_bank = InterBank(chrono=self.__chronometer)
        self.__nbu = NBU(chrono=self.__chronometer)
        self.__visa = Visa(chrono=self.__chronometer)
        self.__mastercard = MasterCard(chrono=self.__chronometer)


class PressCentre(Runner):
    def __init__(self):
        super().__init__()

    def appeal(self, letter):
        pass


if __name__ == '__main__':
    press = PressCentre()



