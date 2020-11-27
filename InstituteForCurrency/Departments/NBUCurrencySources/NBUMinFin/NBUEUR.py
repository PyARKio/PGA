# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.NBUCurrencySources.NBUMinFin.AbsMinFinNBU import ABCMinFin
from Memento.InstituteForCurrency.Departments.NBU_Currency import NBUEURMemento
from Arsenal.Chronicler import log
from datetime import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class NBUEUR(ABCMinFin, NBUEURMemento):
    def __str__(self):
        return 'EUR'

    def check(self):
        if self._pipe_to_nbu.status():
            nbu_week, bid_offer, tbody = self.parser(self._pipe_to_nbu.data['content'])
            if nbu_week and bid_offer and tbody:

                self._struct.time = datetime.now()
                self._struct.official.main = float(bid_offer[0])
                self._struct.official.diff = float(bid_offer[1])
                self._struct.week = float(nbu_week.text)
                self._struct.date = tbody.small.text

                self._insert_obj({'time': self._struct.time,
                                  'official_main': self._struct.official.main,
                                  'official_diff': self._struct.official.diff,
                                  'week': self._struct.week,
                                  'date': self._struct.date})

                log.info(self._struct)
                # log.info(self._get_all_objects())

            else:

                self._struct.time = datetime.now()
                self._struct.official.main = None
                self._struct.official.diff = None
                self._struct.week = None
                self._struct.date = None

                self._insert_obj({'time': self._struct.time,
                                  'official_main': self._struct.official.main,
                                  'official_diff': self._struct.official.diff,
                                  'week': self._struct.week,
                                  'date': self._struct.date})

                log.info(self._struct)
                # log.info(self._get_all_objects())

        else:
            for i, v in self._pipe_to_nbu.errors.items():
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

        import pickle

        with open('NBUEUR.io', 'wb') as f:
            pickle.dump(self._get_all_objects(), f)

        # log.info(self._get_all_objects())
        # self._update_all(data={'YEAR': 1, 'MONTH': 1, 'DAY': 1, 'HOUR': 1})
        # log.info(self._get_all_objects())

        # log.info(letter)
        # # log.info(self._get_spec([{'$group': {'_id': {'day': {'$dayOfYear': '$time'}}, letter: {'$push': '${}'.format(letter)}, 'date': {'$push': '$time'}}}]))
        # log.info(self._get_spec([{'$group': {'_id': None, letter: {'$push': '${}'.format(letter)}, 'date': {'$push': '$time'}}}]))
        # return self._get_spec([{'$group': {'_id': None, letter: {'$push': '${}'.format(letter)}, 'date': {'$push': '$time'}}}])
