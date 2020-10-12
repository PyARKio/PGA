# -- coding: utf-8 --
from __future__ import unicode_literals
from Memento.Memento import BaseMongodbHandler


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class AuctionUSDMemento(BaseMongodbHandler):
    collection_name = 'auction_USD'
    db_fields = ('_id', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')


class AuctionEURMemento(BaseMongodbHandler):
    collection_name = 'auction_EUR'
    db_fields = ('_id', 'time', 'bid_main', 'bid_diff', 'offer_main', 'offer_diff')






