# -- coding: utf-8 --
from __future__ import unicode_literals
from Currencies.BasisForCurrencies.Auction import AbstractAuction
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from datetime import datetime
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Auction(object):
    def __init__(self, source):
        self.__auction = URL(source)
        self.__structure = AbstractAuction()

    def __str__(self):
        return self.__structure.str

    @property
    def get(self):
        if self.__auction.status():
            content = self.__auction.data['content']
            html = BeautifulSoup(content, 'html.parser')
            trs = html.main.tbody.findAll('tr')

            for tr in trs:
                if 'ЧОРНИЙ РИНОК' in tr.a:
                    bid_offer = re.findall(r'[-+]?\d{1,2}\.\d{1,3}', tr.text)
                    self.__structure.time = datetime.now()
                    self.__structure.bid.main = bid_offer[0]
                    self.__structure.bid.diff = bid_offer[1]
                    self.__structure.offer.main = bid_offer[2]
                    self.__structure.offer.diff = bid_offer[3]

            return self.__structure

            # for i, v in self.__currency.data.items():
            #         log.debug(i)
            #         log.debug(v)
        else:
            for i, v in self.__auction.errors.items():
                log.debug(i)
                log.debug(v)

            return self.__auction.errors







