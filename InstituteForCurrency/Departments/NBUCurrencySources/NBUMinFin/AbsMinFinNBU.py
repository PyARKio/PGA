# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureNBU
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
        self._pipe_to_nbu = URL(source)
        self._struct = StructureNBU(currency=self)

    @staticmethod
    def parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        div = main.find(class_='container clearfix')
        tbody = div.tbody
        nbu_c = tbody.find(class_='responsive-hide td-collapsed mfm-text-nowrap mfm-text-right')
        bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', nbu_c.text)
        nbu_week = tbody.find(class_='mfcur-sparkline-indicator')

        return nbu_week, bid_offer, tbody