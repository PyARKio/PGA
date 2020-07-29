# -- coding: utf-8 --
from __future__ import unicode_literals
from abc import ABC, abstractmethod


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractBank(ABC):
    def __init__(self):
        self.time = None
        self.bid = MainDiff()
        self.offer = MainDiff()
        self.week = None

    def __str__(self):
        return 'Time: {}; Bid.main: {}; Bid.diff: {}; Offer.main: {}; Offer.diff: {}; Week: {}'.\
            format(self.time, self.bid.main, self.bid.diff, self.offer.main, self.offer.diff, self.week)


class MainDiff(ABC):
    def __init__(self):
        self.main = None
        self.diff = None


