# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Sources.AbstractSource import AbstractSource
from InstituteForCurrency.Sources.AbstractSource import StructureInterBank
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class InterBank(AbstractSource):
    def __init__(self, source):
        super().__init__()
        self.__ib_usd = URL(source['USD'])
        self.__ib_eur = URL(source['EUR'])

        self.__usd = StructureInterBank(currency='USD')
        self.__eur = StructureInterBank(currency='EUR')

        self._report = {'USD': self.__usd,
                        'EUR': self.__eur}

        self.__delay = randint(self._delay_from, self._delay_to)
        self._get_currency = [self.__get_usd, self.__get_eur]

    @staticmethod
    def __parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        div = main.find(class_='container clearfix')
        tbody = div.tbody
        trs = tbody.findAll('tr')
        bid = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', trs[0].find(class_='active').text)
        offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', trs[1].find(class_='active').text)

        return bid, offer

    def __get_usd(self):
        if self.__ib_usd.status():
            bid, offer = self.__parser(self.__ib_usd.data['content'])

            self.__usd.time = datetime.now()
            self.__usd.bid.main = bid[0]
            self.__usd.bid.diff = bid[1]
            self.__usd.offer.main = offer[0]
            self.__usd.offer.diff = offer[1]

            log.info(self.__usd.str)

            self._report['USD'] = self.__usd

        else:
            for i, v in self.__ib_usd.errors.items():
                log.debug(i)
                log.debug(v)

    def __get_eur(self):
        if self.__ib_eur.status():
            bid, offer = self.__parser(self.__ib_eur.data['content'])

            self.__eur.time = datetime.now()
            self.__eur.bid.main = bid[0]
            self.__eur.bid.diff = bid[1]
            self.__eur.offer.main = offer[0]
            self.__eur.offer.diff = offer[1]

            log.info(self.__eur.str)

            self._report['EUR'] = self.__eur

        else:
            for i, v in self.__ib_eur.errors.items():
                log.debug(i)
                log.debug(v)


if __name__ == '__main__':
    nbu = InterBank({'USD': 'https://minfin.com.ua/ua/currency/mb/',
                     'EUR': 'https://minfin.com.ua/ua/currency/mb/eur/'})
    nbu.check()
    log.info(nbu.appeal(['USD']))
    log.info(nbu.appeal(['EUR']))
    log.info(nbu.appeal(['USD', 'EUR']))
    log.info(nbu.appeal(['USD1']))






