# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AuctionDepartment import Auction
from InstituteForCurrency.Departments.BankDepartment import Bank
from InstituteForCurrency.Departments.InterBankDepartment import InterBank
from InstituteForCurrency.Departments.NBUCurrencyDepartment import NBU
from InstituteForCurrency.Departments.MasterCardDepartment import MasterCard
from InstituteForCurrency.Departments.VisaDepartment import Visa
from Arsenal.Chronometer import Chronometer
from Arsenal.Chronicler import log
import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class PressCentre:
    def __init__(self):
        self.__chronometer = Chronometer()
        self.__chronometer.start()

        self.__auction = Auction(chrono=self.__chronometer)
        self.__bank = Bank(chrono=self.__chronometer)
        self.__inter_bank = InterBank(chrono=self.__chronometer)
        self.__nbu = NBU(chrono=self.__chronometer)
        self.__visa = Visa(chrono=self.__chronometer)
        self.__mastercard = MasterCard(chrono=self.__chronometer)

        self.__departments = {'Question to Auction': self.__auction.question,
                              'Question to Bank': self.__bank.question,
                              'Question to InterBank': self.__inter_bank.question,
                              'Question to NBU': self.__nbu.question,
                              'Question to Visa': self.__visa.question,
                              'Question to MasterCard': self.__mastercard.question}

    def appeal(self, letter):
        answer_to_user = {}
        for key, value in letter.items():
            log.info('')
            log.info('Key: {}'.format(key))
            log.info('Value: {}'.format(value))
            if self.__departments.get(key):
                answer_to_user[key] = self.__departments[key](value)
        return answer_to_user


if __name__ == '__main__':
    press = PressCentre()
    # log.debug(press.appeal({'Question to Auction': {'MinFin': {'USD': '', 'EUR': ''}}}))
    log.debug(press.appeal({'Question to Bank': {'MinFin': {'EUR': {'datetime': {'from': datetime.datetime(2020, 10, 15, 22, 2, 18, 961000),
                                                                                 'to': datetime.datetime(2020, 10, 16, 7, 2, 18, 961000)},
                                                                    'bid_main': [], 'bid_diff': [],
                                                                    'offer_main': [], 'offer_diff': [],
                                                                    'week': []}
                                                            }}}))
    # log.debug(press.appeal({'Question to InterBank': {'MinFin': {'USD': '', 'EUR': ''}}}))
    # log.debug(press.appeal({'Question to NBU': {'MinFin': {'USD': '', 'EUR': ''}}}))
    # log.debug(press.appeal({'Question to Visa': {'MinFin': {'USD': '', 'EUR': ''}}}))
    # log.debug(press.appeal({'Question to MasterCard': {'MinFin': {'USD': '', 'EUR': ''}}}))
