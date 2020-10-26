# -- coding: utf-8 --
from __future__ import unicode_literals
from Memento.Memento import BaseMongodbHandler


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MasterCardCuratorMemento(BaseMongodbHandler):
    collection_name = 'mastercard_url'
    db_fields = ('_id', 'currency',
                 'minfin_usd', 'minfin_eur',
                 'kurs_usd', 'kurs_eur',
                 'finance_usd', 'finance_eur')


class MasterCardUSDMemento(BaseMongodbHandler):
    collection_name = 'mastercard_USD'
    db_fields = ('_id', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')


class MasterCardEURMemento(BaseMongodbHandler):
    collection_name = 'mastercard_EUR'
    db_fields = ('_id', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')
