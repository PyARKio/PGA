# -- coding: utf-8 --
from __future__ import unicode_literals
from Memento.Memento import BaseMongodbHandler


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class VisaCuratorMemento(BaseMongodbHandler):
    collection_name = 'visa_url'
    db_fields = ('_id', 'currency',
                 'minfin_usd', 'minfin_eur',
                 'kurs_usd', 'kurs_eur',
                 'finance_usd', 'finance_eur')


class VisaUSDMemento(BaseMongodbHandler):
    collection_name = 'visa_USD'
    db_fields = ('_id', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')


class VisaEURMemento(BaseMongodbHandler):
    collection_name = 'visa_EUR'
    db_fields = ('_id', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')
