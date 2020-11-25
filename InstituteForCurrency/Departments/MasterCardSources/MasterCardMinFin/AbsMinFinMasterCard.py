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
            return False
        try:
            tr = div.tbody.tr
        except Exception as err:
            return False

        tds = tr.findAll('td')
        bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', tds[3].text)

        return bid_offer
