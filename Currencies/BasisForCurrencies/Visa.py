# -- coding: utf-8 --
from __future__ import unicode_literals
from .AbstractCurrency import MainDiff


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractVisa(object):
    def __init__(self):
        self.time = None
        self.bid = MainDiff('Bid')
        self.offer = MainDiff('Offer')

    @property
    def str(self):
        return 'Time: {}; {}; {}'.format(self.time, self.bid, self.offer)




