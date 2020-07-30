# -- coding: utf-8 --
from __future__ import unicode_literals
from Currencies.BasisForCurrencies.InterBank import AbstractInterBank
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class InterBank(object):
    def __init__(self, source):
        self.__interbank = URL(source)
        self.__structure = AbstractInterBank()

    def __str__(self):
        return self.__structure.str

    @property
    def get(self):
        if self.__interbank.status():
            content = self.__interbank.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tbody = div.tbody
            trs = tbody.findAll('tr')

            bid = re.findall(r'\S\d{1,2}\.\d{1,4}', trs[0].find(class_='active').text)
            offer = re.findall(r'\S\d{1,2}\.\d{1,4}', trs[1].find(class_='active').text)

            self.__structure.time = str(datetime.now())
            self.__structure.bid.main = bid[0]
            self.__structure.bid.diff = bid[1]
            self.__structure.offer.main = offer[0]
            self.__structure.offer.diff = offer[1]

            # for i, v in self.__banks.data.items():
            #         log.debug(i)
            #         log.debug(v)

            return self.__structure
        else:
            for i, v in self.__interbank.errors.items():
                log.debug(i)
                log.debug(v)

            return self.__interbank.errors






