# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AbstractSource import AbstractSource
from InstituteForCurrency.Departments.AbstractSource import StructureAuction
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
        self._pipe_to_auction = URL(source)
        self._struct = StructureAuction(currency=self)

    @staticmethod
    def parser(content):
        html = BeautifulSoup(content, 'html.parser')
        try:
            trs = html.main.tbody.findAll('tr')
        except Exception as err:
            return [None, None, None, None]
        for tr in trs:
            if 'ЧОРНИЙ РИНОК' in tr.a:
                log.info(tr.text)
                data = re.findall(r'[-+]?\d{1,2}\.\d{1,4}', tr.text)
                log.info(data)
                # TODO Fix it
                if len(data) < 2:
                    return [None, None, None, None]

                data_float = []
                for d in data:
                    data_float.append(float(d))
                return data_float
        return [None, None, None, None]
