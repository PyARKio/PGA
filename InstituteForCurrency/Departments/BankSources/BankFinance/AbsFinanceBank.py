# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureBank
from Arsenal.URL_Object import URL
from bs4 import BeautifulSoup
import re


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
        div = main.find(class_='container clearfix')
        tbody = div.tbody

        td_bid_offer = tbody.find(class_='mfm-text-nowrap')
        bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_bid_offer.text)
        td_week = tbody.find(class_='mfcur-sparkline-indicator')
        week = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', td_week.text)

        return bid_offer, week
