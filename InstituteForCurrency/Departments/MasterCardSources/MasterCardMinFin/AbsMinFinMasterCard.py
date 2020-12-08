# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureMasterCard
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
        self._pipe_to_mastercard = URL(source)
        self._struct = StructureMasterCard(currency=self)

    @staticmethod
    def parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        try:
            div = main.find(class_='container clearfix')
        except Exception as err:
            return [None, None, None, None]
        try:
            tr = div.tbody.tr
        except Exception as err:
            return [None, None, None, None]

        tds = tr.findAll('td')
        try:
            bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', tds[3].text)
        except Exception as err:
            return [None, None, None, None]

        bid_offer_float = []
        for b in bid_offer:
            bid_offer_float.append(float(b))
        return bid_offer_float
