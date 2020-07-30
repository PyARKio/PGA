# -- coding: utf-8 --
from __future__ import unicode_literals
from Currencies.BasisForCurrencies.NBU import AbstractNBU
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class NBU(object):
    def __init__(self, source):
        self.__nbu = URL(source)
        self.__structure = AbstractNBU()

    def __str__(self):
        return self.__structure.str

    @property
    def get(self):
        if self.__nbu.status():
            content = self.__nbu.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tbody = div.tbody

            nbu_c = tbody.find(class_='responsive-hide td-collapsed mfm-text-nowrap mfm-text-right')
            bid_offer = re.findall(r'\d{1,2}\.\d{1,4}', nbu_c.text)

            nbu_week = tbody.find(class_='mfcur-sparkline-indicator icon-up-open')

            self.__structure.time = datetime.now()
            self.__structure.official.main = bid_offer[0]
            self.__structure.official.diff = bid_offer[1]
            self.__structure.week = nbu_week.text
            self.__structure.date = tbody.small.text

            return self.__structure

            # for i, v in self.__nbu.data.items():
            #         log.debug(i)
            #         log.debug(v)
        else:
            for i, v in self.__nbu.errors.items():
                log.debug(i)
                log.debug(v)

            return self.__nbu.errors



