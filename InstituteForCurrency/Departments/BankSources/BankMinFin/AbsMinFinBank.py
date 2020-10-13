# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureBank
from Memento.InstituteForCurrency.Sources.Bank import BankUSDMemento
from Arsenal.Chronicler import log
from Arsenal.URL_Object import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class BankUSD(AbstractSource, BankUSDMemento):
    def __init__(self, source, chrono):
        super().__init__()
        self.__chronometer = chrono
        self.__bank_usd = URL(source['USD'])
        self.__bank_eur = URL(source['EUR'])

        self.__usd = StructureBank(currency='USD')
        self.__eur = StructureBank(currency='EUR')

        self._report = {'USD': self.__usd,
                        'EUR': self.__eur}

        self._get_currency = [self.__get_usd]

        self._add_mark()

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

            self.insert_obj({'time': self.__usd.time,
                             'bid_main': self.__usd.bid.main,
                             'bid_diff': self.__usd.bid.diff,
                             'offer_main': self.__usd.offer.main,
                             'offer_diff': self.__usd.offer.diff,
                             'week': self.__usd.week})

            log.info(self.__usd.str)
            log.info(self.get_all_objects())

            self._report['USD'] = self.__usd

        else:
            for i, v in self.__bank_usd.errors.items():
                log.debug(i)
                log.debug(v)

    def _add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self._set_delay(), 'CallBack': self.check})


