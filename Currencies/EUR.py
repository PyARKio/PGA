# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from BasisForCurrencies.AbstractCurrency import Currency
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from utilits.interrupt import Interrupt
from random import randint
from Currencies.EUR_Utilits.Bank import Bank
from Currencies.EUR_Utilits.Auction import Auction
from Currencies.EUR_Utilits.NBU import NBU
from Currencies.EUR_Utilits.InterBank import InterBank
from Currencies.EUR_Utilits.Visa import Visa
from Currencies.EUR_Utilits.MasterCard import MasterCard


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class EUR(Currency):
    Currency = '-/-'
    Retail = '-/-'
    Auction = '-/-'
    NBU = '-/-'
    Visa = '-/-'
    MasterCard = '-/-'

    def __init__(self):
        super().__init__()
        log.debug(self)
        self.__timer = Interrupt(name=self, callback_handler=self.get_data, delay=(670, 1237), random_mode=True)
        self.__timer.go_go()
        log.info(self.__timer.delay)

        # WARNING    \S\d{1,2}\.\d{1,3} ['27.550', '0.050', '0.000', '27.800']
        self.__bank = Bank('https://minfin.com.ua/ua/currency/banks/eur/')
        self.__auction = Auction('https://minfin.com.ua/ua/currency/eur/')
        self.__nbu = NBU('https://minfin.com.ua/ua/currency/nbu/eur/')
        self.__interbank = InterBank('https://minfin.com.ua/ua/currency/mb/eur/')
        self.__visa = Visa('https://minfin.com.ua/ua/currency/visa/eur/')
        self.__mastercard = MasterCard('https://minfin.com.ua/ua/currency/mastercard/eur/')

    @classmethod
    def __str__(cls):
        return 'Card for {}'.format(cls.__name__)

    # WARNING    \S\d{1,2}\.\d{1,3} ['27.550', '0.050', '0.000', '27.800']
    def get_data(self):
        log.info(self.__bank.get)
        log.info(self.__bank)

        log.info(self.__auction.get)
        log.info(self.__auction)

        log.info(self.__nbu.get)
        log.info(self.__nbu)

        log.info(self.__interbank.get)
        log.info(self.__interbank)

        log.info(self.__visa.get)
        log.info(self.__visa)

        log.info(self.__mastercard.get)
        log.info(self.__mastercard)


if __name__ == '__main__':
    import time

    usd = EUR()
    usd.get_data()
    while True:
        sleep = 1000
        time.sleep(sleep)

