# -- coding: utf-8 --
from __future__ import unicode_literals
from .AbstractCurrency import MainDiff


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AbstractNBU(object):
    def __init__(self):
        self.time = None
        self.official = MainDiff('Official')
        self.week = None
        self.date = None

    @property
    def str(self):
        return 'Time: {}; {}; Week: {}; Date: {}'.format(self.time, self.official, self.week, self.date)





