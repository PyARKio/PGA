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
            if bid_offer:

                self._struct.time = datetime.now()
                self._struct.bid.main = float(bid_offer[0])
                self._struct.bid.diff = float(bid_offer[1])
                self._struct.offer.main = float(bid_offer[3])
                self._struct.offer.diff = float(bid_offer[2])

                self._insert_obj({'time': self._struct.time,
                                  'bid_main': self._struct.bid.main,
                                  'bid_diff': self._struct.bid.diff,
                                  'offer_main': self._struct.offer.main,
                                  'offer_diff': self._struct.offer.diff})

                log.info(self._struct)
                # log.info(self._get_all_objects())

            else:

                self._struct.time = datetime.now()
                self._struct.bid.main = None
                self._struct.bid.diff = None
                self._struct.offer.main = None
                self._struct.offer.diff = None

                self._insert_obj({'time': self._struct.time,
                                  'bid_main': self._struct.bid.main,
                                  'bid_diff': self._struct.bid.diff,
                                  'offer_main': self._struct.offer.main,
                                  'offer_diff': self._struct.offer.diff})

                log.info(self._struct)
                # log.info(self._get_all_objects())

        else:
            for i, v in self._pipe_to_mastercard.errors.items():
                log.debug(i)
                log.debug(v)

        self._add_mark()

    def appeal(self, letter):
        """
        - get current values
        - get from to (how can I do it?)

        :param letter:
        :return:
        """

        # log.info(self._get_all_objects())
        # self._update_all(data={'YEAR': 1, 'MONTH': 1, 'DAY': 1, 'HOUR': 1})
        # log.info(self._get_all_objects())

        log.info(letter)
        # log.info(self._get_spec([{'$group': {'_id': {'day': {'$dayOfYear': '$time'}}, letter: {'$push': '${}'.format(letter)}, 'date': {'$push': '$time'}}}]))
        log.info(self._get_spec([{'$group': {'_id': None, letter: {'$push': {'$convert': {'input': '${}'.format(letter), 'to': "decimal"}}}, 'date': {'$push': '$time'}}}]))
        return self._get_spec([{'$group': {'_id': None, letter: {'$push': '${}'.format(letter)}, 'date': {'$push': '$time'}}}])
