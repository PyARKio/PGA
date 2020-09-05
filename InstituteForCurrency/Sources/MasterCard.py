# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Sources.AbstractSource import AbstractSource
from InstituteForCurrency.Sources.AbstractSource import StructureMasterCard
from Arsenal.log_settings import log
from Arsenal.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MasterCard(AbstractSource):
    def __init__(self, source, chrono):
        super().__init__()
        self.__chronometer = chrono
        self.__mc_usd = URL(source['USD'])
        self.__mc_eur = URL(source['EUR'])

        self.__usd = StructureMasterCard(currency='USD')
        self.__eur = StructureMasterCard(currency='EUR')

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
        tr = div.tbody.tr
        tds = tr.findAll('td')
        bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', tds[3].text)

        return bid_offer

    def __get_usd(self):
        if self.__mc_usd.status():
            bid_offer = self.__parser(self.__mc_usd.data['content'])

            self.__usd.time = datetime.now()
            self.__usd.bid.main = bid_offer[0]
            self.__usd.bid.diff = bid_offer[1]
            self.__usd.offer.main = bid_offer[3]
            self.__usd.offer.diff = bid_offer[2]

            log.info(self.__usd.str)

            self._report['USD'] = self.__usd

        else:
            for i, v in self.__mc_usd.errors.items():
                log.debug(i)
                log.debug(v)

    def __get_eur(self):
        if self.__mc_eur.status():
            bid_offer = self.__parser(self.__mc_eur.data['content'])

            self.__eur.time = datetime.now()
            self.__eur.bid.main = bid_offer[0]
            self.__eur.bid.diff = bid_offer[1]
            self.__eur.offer.main = bid_offer[3]
            self.__eur.offer.diff = bid_offer[2]

            log.info(self.__eur.str)

            self._report['EUR'] = self.__eur

        else:
            for i, v in self.__mc_eur.errors.items():
                log.debug(i)
                log.debug(v)

    def _add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self._set_delay(), 'CallBack': self.check})




