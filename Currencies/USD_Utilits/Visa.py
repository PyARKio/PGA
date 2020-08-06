# -- coding: utf-8 --
from __future__ import unicode_literals
from Currencies.BasisForCurrencies.Visa import AbstractVisa
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Visa(object):
    def __init__(self, source):
        self.__visa = URL(source)
        self.__structure = AbstractVisa()

    def __str__(self):
        return self.__structure.str

    @property
    def get(self):
        if self.__visa.status():
            content = self.__visa.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tr = div.tbody.tr
            tds = tr.findAll('td')

            bid_offer = re.findall(r'\d{1,2}\.\d{1,4}', tds[2].text)

            self.__structure.time = datetime.now()
            self.__structure.bid.main = bid_offer[0]
            self.__structure.bid.diff = bid_offer[1]
            self.__structure.offer.main = bid_offer[3]
            self.__structure.offer.diff = bid_offer[2]

            # for i, v in self.__banks.data.items():
            #         log.debug(i)
            #         log.debug(v)

            return self.__structure
        else:
            for i, v in self.__visa.errors.items():
                log.debug(i)
                log.debug(v)

            return self.__visa.errors






