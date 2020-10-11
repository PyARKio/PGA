# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Sources.AbstractSource import AbstractSource
from InstituteForCurrency.Sources.AbstractSource import StructureAuction
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


class Auction(AbstractSource):
    def __init__(self, source, chrono):
        super().__init__()
        self.__chronometer = chrono
        self.__auction_usd = URL(source['USD'])
        self.__auction_eur = URL(source['EUR'])

        self.__usd = StructureAuction(currency='USD')
        self.__eur = StructureAuction(currency='EUR')

        self._report = {'USD': self.__usd,
                        'EUR': self.__eur}

        self.__delay = randint(self._delay_from, self._delay_to)
        self._get_currency = [self.__get_usd, self.__get_eur]

        self._add_mark()

    def __get_usd(self):
        if self.__auction_usd.status():
            content = self.__auction_usd.data['content']
            html = BeautifulSoup(content, 'html.parser')
            trs = html.main.tbody.findAll('tr')

            for tr in trs:
                if 'ЧОРНИЙ РИНОК' in tr.a:
                    bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', tr.text)
                    self.__usd.time = datetime.now()
                    self.__usd.bid.main = bid_offer[0]
                    self.__usd.bid.diff = bid_offer[1]
                    self.__usd.offer.main = bid_offer[2]
                    self.__usd.offer.diff = bid_offer[3]

            log.info(self.__usd.str)

            self._report['USD'] = self.__usd

        else:
            for i, v in self.__auction_usd.errors.items():
                log.debug(i)
                log.debug(v)

    def __get_eur(self):
        if self.__auction_eur.status():
            content = self.__auction_eur.data['content']
            html = BeautifulSoup(content, 'html.parser')
            trs = html.main.tbody.findAll('tr')

            for tr in trs:
                if 'ЧОРНИЙ РИНОК' in tr.a:
                    bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', tr.text)
                    self.__eur.time = datetime.now()
                    self.__eur.bid.main = bid_offer[0]
                    self.__eur.bid.diff = bid_offer[1]
                    self.__eur.offer.main = bid_offer[2]
                    self.__eur.offer.diff = bid_offer[3]

            log.info(self.__eur.str)

            self._report['EUR'] = self.__eur

        else:
            for i, v in self.__auction_eur.errors.items():
                log.debug(i)
                log.debug(v)

    def _add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self._set_delay(), 'CallBack': self.check})



