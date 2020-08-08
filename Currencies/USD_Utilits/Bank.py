# -- coding: utf-8 --
from __future__ import unicode_literals
from Currencies.BasisForCurrencies.Bank import AbstractBank
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Bank(object):
    def __init__(self, source):
        self.__banks = URL(source)
        self.__structure = AbstractBank()

    def __str__(self):
        return self.__structure.str

    @property
    def get(self):
        if self.__banks.status():
            content = self.__banks.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tbody = div.tbody

            td_bid_offer = tbody.find(class_='mfm-text-nowrap')
            bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_bid_offer.text)
            td_week = tbody.find(class_='mfcur-sparkline-indicator')
            week = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_week.text)

            # https://tproger.ru/translations/regular-expression-python/

            self.__structure.time = datetime.now()
            self.__structure.bid.main = bid_offer[0]
            self.__structure.bid.diff = bid_offer[1]
            self.__structure.offer.main = bid_offer[3]
            self.__structure.offer.diff = bid_offer[2]
            self.__structure.week = week[0]

            # for i, v in self.__banks.data.items():
            #         log.debug(i)
            #         log.debug(v)

            return self.__structure
        else:
            for i, v in self.__banks.errors.items():
                log.debug(i)
                log.debug(v)

            return self.__banks.errors


if __name__ == '__main__':
    bank = Bank('https://minfin.com.ua/ua/currency/banks/usd/')
    bank_get = bank.get
    log.info(bank_get.offer)
    log.info(bank_get.offer.main)





