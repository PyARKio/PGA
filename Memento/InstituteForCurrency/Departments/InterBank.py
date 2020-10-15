# -- coding: utf-8 --
from __future__ import unicode_literals
from Memento.Memento import BaseMongodbHandler


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class InterBankCuratorMemento(BaseMongodbHandler):
    collection_name = 'interbank_url'
    db_fields = ('_id', 'currency',
                 'minfin_usd', 'minfin_eur',
                 'kurs_usd', 'kurs_eur',
                 'finance_usd', 'finance_eur')


class InterBankUSDMemento(BaseMongodbHandler):
    collection_name = 'interbank_USD'
    db_fields = ('_id', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')


class InterBankEURMemento(BaseMongodbHandler):
    collection_name = 'interbank_EUR'
    db_fields = ('_id', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')
