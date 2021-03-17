# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureBank
from Arsenal.URL_Object import URL
from bs4 import BeautifulSoup
import re
from Arsenal.Chronicler import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class ABCMinFin(AbstractSource):
    def __init__(self, source, chrono):
        super().__init__(chrono)
        self._pipe_to_bank = URL(source)
        self._struct = StructureBank(currency=self)

    @staticmethod
    def parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        try:
            div = main.find(class_='container clearfix')
        except Exception as err:
            log.error(content)
            return False

        tbody = div.tbody

        try:
            td_bid_offer = tbody.find(class_='mfm-text-nowrap')
        except Exception as err:
            return [None, None, None, None], [None]

        try:
            bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_bid_offer.text)
        except Exception as err:
            return [None, None, None, None], [None]

        try:
            td_week = tbody.find(class_='mfcur-sparkline-indicator')
        except Exception as err:
            return [None, None, None, None], [None]
        try:
            week = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_week.text)
        except Exception as err:
            return [None, None, None, None], [None]

        bid_offer_float = []
        week_float = []
        for b in bid_offer:
            bid_offer_float.append(float(b))
        for w in week:
            week_float.append(float(w))

        return bid_offer, week
