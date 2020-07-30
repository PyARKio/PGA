# -- coding: utf-8 --
from __future__ import unicode_literals
from .AbstractCurrency import MainDiff


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractBank(object):
    def __init__(self):
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')
        self.week = None

    @property
    def str(self):
        return 'Time: {}; {}; {}; Week: {}'.format(self.time, self.bid, self.offer, self.week)




