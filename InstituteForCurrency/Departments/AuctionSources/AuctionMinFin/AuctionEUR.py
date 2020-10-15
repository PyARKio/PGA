# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AuctionSources.AuctionMinFin.AbsMinFinAuction import ABCMinFin
from Memento.InstituteForCurrency.Departments.Auction import AuctionEURMemento
from Arsenal.Chronicler import log
from datetime import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AuctionEUR(ABCMinFin, AuctionEURMemento):
    def __str__(self):
        return 'EUR'

    def check(self):
        if self._pipe_to_auction.status():
            bid_offer = self.parser(self._pipe_to_auction.data['content'])

            self._struct.time = datetime.now()
            self._struct.bid.main = bid_offer[0]
            self._struct.bid.diff = bid_offer[1]
            self._struct.offer.main = bid_offer[2]
            self._struct.offer.diff = bid_offer[3]

            self.insert_obj({'time': self._struct.time,
                             'bid_main': self._struct.bid.main,
                             'bid_diff': self._struct.bid.diff,
                             'offer_main': self._struct.offer.main,
                             'offer_diff': self._struct.offer.diff})

            log.info(self._struct)
            log.info(self.get_all_objects())

        else:
            for i, v in self._pipe_to_auction.errors.items():
                log.debug(i)
                log.debug(v)

        self._add_mark()


if __name__ == '__main__':
    from Arsenal.Chronometer import Chronometer

    chronometer = Chronometer()
    chronometer.start()
    bank = AuctionEUR(source='https://minfin.com.ua/ua/currency/eur/',
                      chrono=chronometer)
