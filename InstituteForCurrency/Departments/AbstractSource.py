# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractSource(ABC):
    def __init__(self, chrono):
        self.__chronometer = chrono
        self._delay_from = 1
        self._delay_to = 59
        self._delay = 0

        self._add_mark()

    @abstractmethod
    def check(self):
        ...

    def appeal(self, letter):
        ...

    def _set_delay(self):
        self._delay += randint(self._delay_from, self._delay_to)
        if self._delay > 59:
            self._delay -= 60
        return self._delay

    def _add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self._set_delay(), 'CallBack': self.check})


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

    def __str__(self):
        return 'Currency: {}; Time: {}; {}; Week: {}; Date: {}'.\
            format(self.currency, self.time, self.official, self.week, self.date)


class StructureInterBank(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    def __str__(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)


class StructureAuction(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    def __str__(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)


class StructureBank(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')
        self.week = None

    def __str__(self):
        return 'Currency: {}; Time: {}; {}; {}; Week: {}'.format(self.currency, self.time, self.bid, self.offer, self.week)


class StructureMasterCard(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    def __str__(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)


class StructureVisa(object):
    def __init__(self, currency=None):
        self.currency = currency
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    def __str__(self):
        return 'Currency: {}; Time: {}; {}; {}'.format(self.currency, self.time, self.bid, self.offer)







