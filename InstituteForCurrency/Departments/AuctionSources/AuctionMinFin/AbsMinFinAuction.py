# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureAuction
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
        self._pipe_to_auction = URL(source)
        self._struct = StructureAuction(currency=self)

    @staticmethod
    def parser(content):
        html = BeautifulSoup(content, 'html.parser')
        trs = html.main.tbody.findAll('tr')
        for tr in trs:
            if 'ЧОРНИЙ РИНОК' in tr.a:
                return re.findall(r'[-+]?\d{1,2}\.\d{1,3}', tr.text)
