# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureNBU
from Arsenal.Chronicler import log
from Arsenal.URL_Object import URL
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class NBU(AbstractSource):
    def __init__(self, source, chrono):
        super().__init__()
        self.__chronometer = chrono
        self.__nbu_usd = URL(source['USD'])
        self.__nbu_eur = URL(source['EUR'])

        self.__usd = StructureNBU(currency='USD')
        self.__eur = StructureNBU(currency='EUR')

        self._report = {'USD': self.__usd,
                        'EUR': self.__eur}

        self.__delay = randint(self._delay_from, self._delay_to)
        self._get_currency = [self.__get_usd, self.__get_eur]

        self._add_mark()

    @staticmethod
    def __parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        div = main.find(class_='container clearfix')
        tbody = div.tbody
        nbu_c = tbody.find(class_='responsive-hide td-collapsed mfm-text-nowrap mfm-text-right')
        bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', nbu_c.text)
        nbu_week = tbody.find(class_='mfcur-sparkline-indicator')

        return nbu_week, bid_offer, tbody

    def __get_usd(self):
        if self.__nbu_usd.status():
            nbu_week, bid_offer, tbody = self.__parser(self.__nbu_usd.data['content'])

            self.__usd.time = datetime.now()
            self.__usd.official.main = bid_offer[0]
            self.__usd.official.diff = bid_offer[1]
            self.__usd.week = nbu_week.text
            self.__usd.date = tbody.small.text

            log.info(self.__usd.str)

            self._report['USD'] = self.__usd

        else:
            for i, v in self.__nbu_usd.errors.items():
                log.debug(i)
                log.debug(v)

    def __get_eur(self):
        if self.__nbu_eur.status():
            nbu_week, bid_offer, tbody = self.__parser(self.__nbu_eur.data['content'])

            self.__eur.time = datetime.now()
            self.__eur.official.main = bid_offer[0]
            self.__eur.official.diff = bid_offer[1]
            self.__eur.week = nbu_week.text
            self.__eur.date = tbody.small.text

            log.info(self.__eur.str)

            self._report['EUR'] = self.__eur

        else:
            for i, v in self.__nbu_eur.errors.items():
                log.debug(i)
                log.debug(v)

    def _add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self._set_delay(), 'CallBack': self.check})


