# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Sources.AbstractSource import AbstractSource
from InstituteForCurrency.Sources.AbstractSource import StructureBank
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Bank(AbstractSource):
    def __init__(self, source):
        super().__init__()
        self.__bank_usd = URL(source['USD'])
        self.__bank_eur = URL(source['EUR'])

        self.__usd = StructureBank(currency='USD')
        self.__eur = StructureBank(currency='EUR')

        self._report = {'USD': self.__usd,
                        'EUR': self.__eur}

        self._get_currency = [self.__get_usd, self.__get_eur]

    @staticmethod
    def __parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        div = main.find(class_='container clearfix')
        tbody = div.tbody

        td_bid_offer = tbody.find(class_='mfm-text-nowrap')
        bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_bid_offer.text)
        td_week = tbody.find(class_='mfcur-sparkline-indicator')
        week = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_week.text)

        return bid_offer, week

    def __get_usd(self):
        if self.__bank_usd.status():
            bid_offer, week = self.__parser(self.__bank_usd.data['content'])

            self.__usd.time = datetime.now()
            self.__usd.bid.main = bid_offer[0]
            self.__usd.bid.diff = bid_offer[1]
            self.__usd.offer.main = bid_offer[3]
            self.__usd.offer.diff = bid_offer[2]
            self.__usd.week = week[0]

            log.info(self.__usd.str)

            self._report['USD'] = self.__usd

        else:
            for i, v in self.__bank_usd.errors.items():
                log.debug(i)
                log.debug(v)

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


if __name__ == '__main__':
    nbu = Bank({'USD': 'https://minfin.com.ua/ua/currency/banks/usd/',
                'EUR': 'https://minfin.com.ua/ua/currency/banks/eur/'})
    nbu.check()
    log.info(nbu.appeal(['USD']))
    log.info(nbu.appeal(['EUR']))
    log.info(nbu.appeal(['USD', 'EUR']))
    log.info(nbu.appeal(['USD1']))

