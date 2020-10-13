# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from abc import ABC, abstractmethod
from Arsenal.Chronicler import log
from random import randint


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractSource(ABC):
    def __init__(self):
        self._delay_from = 1
        self._delay_to = 59
        self._delay = 0

        self._report = {}
        self._get_currency = []

    def _set_delay(self):
        self._delay += randint(self._delay_from, self._delay_to)
        if self._delay > 59:
            self._delay -= 60
        return self._delay

    def check(self):
        for currency in self._get_currency:
            currency()
        self._add_mark()

    def appeal(self, letter):
        response = {}
        for key in letter:
            if key in self._report.keys():
                response[key] = self._report[key]
        return response

    def _add_mark(self):
        pass


class MainDiff(object):
    def __init__(self, name):
        self.__name = name
        self.main = None
        self.diff = None

    def __str__(self):
        return '{}.Main: {}; {}.Diff: {}'.format(self.__name, self.main, self.__name, self.diff)


class StructureNBU(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.official = MainDiff('Official')
        self.week = None
        self.date = None

    @property
    def str(self):
        return 'Currency: {}; Time: {}; {}; Week: {}; Date: {}'.\
            format(self.currency, self.time, self.official, self.week, self.date)


class StructureInterBank(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    @property
    def str(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)


class StructureAuction(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    @property
    def str(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)


class StructureBank(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')
        self.week = None

    @property
    def str(self):
        return 'Currency: {}; Time: {}; {}; {}; Week: {}'.format(self.currency, self.time, self.bid, self.offer, self.week)


class StructureMasterCard(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    @property
    def str(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)


class StructureVisa(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    @property
    def str(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)







