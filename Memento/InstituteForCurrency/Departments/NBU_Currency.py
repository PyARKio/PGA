# -- coding: utf-8 --
from __future__ import unicode_literals
from Memento.Memento import BaseMongodbHandler


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class NBUCuratorMemento(BaseMongodbHandler):
    collection_name = 'nbu_url'
    db_fields = ('_id', 'currency',
                 'minfin_usd', 'minfin_eur',
                 'kurs_usd', 'kurs_eur',
                 'finance_usd', 'finance_eur')


class NBUUSDMemento(BaseMongodbHandler):
    collection_name = 'nbu_USD'
    db_fields = ('_id', 'time', 'official_main', 'official_diff', 'week', 'date')


class NBUEURMemento(BaseMongodbHandler):
    collection_name = 'nbu_EUR'
    db_fields = ('_id', 'time', 'official_main', 'official_diff', 'week', 'date')
