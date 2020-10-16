# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.BankSources.BankMinFin.AbsMinFinBank import ABCMinFin
from Memento.InstituteForCurrency.Departments.Bank import BankEURMemento
from Arsenal.Chronicler import log
from datetime import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class BankEUR(ABCMinFin, BankEURMemento):
    def __str__(self):
        return 'EUR'

    def check(self):
        if self._pipe_to_bank.status():
            bid_offer, week = self.parser(self._pipe_to_bank.data['content'])

            self._struct.time = datetime.now()
            self._struct.bid.main = bid_offer[0]
            self._struct.bid.diff = bid_offer[1]
            self._struct.offer.main = bid_offer[3]
            self._struct.offer.diff = bid_offer[2]
            self._struct.week = week[0]

            self._insert_obj({'time': self._struct.time,
                              'bid_main': self._struct.bid.main,
                              'bid_diff': self._struct.bid.diff,
                              'offer_main': self._struct.offer.main,
                              'offer_diff': self._struct.offer.diff,
                              'week': self._struct.week})

            log.info(self._struct)
            log.info(self._get_all_objects())

        else:
            for i, v in self._pipe_to_bank.errors.items():
                log.debug(i)
                log.debug(v)

        self._add_mark()

    def appeal(self, letter):
        log.debug(letter)
        answer_for_curator = self._get_all_objects()
        for d in answer_for_curator:
            if letter['datetime']['from'] < d['time'] < letter['datetime']['to']:
                log.info(d)
        return answer_for_curator


if __name__ == '__main__':
    from Arsenal.Chronometer import Chronometer

    chronometer = Chronometer()
    chronometer.start()
    bank = BankEUR(source='https://minfin.com.ua/ua/currency/banks/eur/',
                   chrono=chronometer)
