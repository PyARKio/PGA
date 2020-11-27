# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureInterBank
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
        self._pipe_to_interbank = URL(source)
        self._struct = StructureInterBank(currency=self)

    @staticmethod
    def parser(content):
        html = BeautifulSoup(content, 'html.parser')
        main = html.main
        try:
            div = main.find(class_='container clearfix')
        except Exception as err:
            return False
        tbody = div.tbody

        try:
            trs = tbody.findAll('tr')
        except Exception as err:
            return False

        bid = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', trs[0].find(class_='active').text)
        offer = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', trs[1].find(class_='active').text)

        return bid, offer
