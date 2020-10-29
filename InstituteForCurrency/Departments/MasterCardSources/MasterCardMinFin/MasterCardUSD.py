# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.MasterCardSources.MasterCardMinFin.AbsMinFinMasterCard import ABCMinFin
from Memento.InstituteForCurrency.Departments.MasterCard import MasterCardUSDMemento
from Arsenal.Chronicler import log
from datetime import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MasterCardUSD(ABCMinFin, MasterCardUSDMemento):
    def __str__(self):
        return 'USD'

    def check(self):
        if self._pipe_to_mastercard.status():
            bid_offer = self.parser(self._pipe_to_mastercard.data['content'])

            self._struct.time = datetime.now()
            self._struct.bid.main = bid_offer[0]
            self._struct.bid.diff = bid_offer[1]
            self._struct.offer.main = bid_offer[3]
            self._struct.offer.diff = bid_offer[2]

            self._insert_obj({'YEAR': self._struct.time.year,
                              'MONTH': self._struct.time.month,
                              'DAY': self._struct.time.day,
                              'HOUR': self._struct.time.hour,
                              'time': self._struct.time,
                              'bid_main': self._struct.bid.main,
                              'bid_diff': self._struct.bid.diff,
                              'offer_main': self._struct.offer.main,
                              'offer_diff': self._struct.offer.diff})

            log.info(self._struct)
            log.info(self._get_all_objects())

        else:
            for i, v in self._pipe_to_mastercard.errors.items():
                log.debug(i)
                log.debug(v)

        self._add_mark()

    def appeal(self, letter):
        ...
