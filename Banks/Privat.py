# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from BasisForCurrencies.AbstractCurrency import Currency
from Arsenal.Chronicler import log
from Arsenal.interrupt import Interrupt
from Banks.PrivatBank_utilits.Currency import CurrenciesInBank


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class PrivatBank(Currency):
    USD = ''
    EUR = ''

    def __init__(self):
        super().__init__()
        log.debug(self)
        self.__timer = Interrupt(name=self, callback_handler=self.get_data, delay=(670, 1237), random_mode=True)
        self.__timer.go_go()
        log.info(self.__timer.delay)

        # WARNING    \S\d{1,2}\.\d{1,3} ['27.550', '0.050', '0.000', '27.800']
        self.__bank = CurrenciesInBank('https://minfin.com.ua/ua/company/privatbank/currency/')

    @classmethod
    def __str__(cls):
        return 'Card for {}'.format(cls.__name__)

    # WARNING    \S\d{1,2}\.\d{1,3} ['27.550', '0.050', '0.000', '27.800']
    def get_data(self):
        pass


if __name__ == '__main__':
    import time

    usd = PrivatBank()
    usd.get_data()
    while True:
        sleep = 1000
        time.sleep(sleep)

