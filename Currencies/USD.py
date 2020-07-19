# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from .AbstractCurrency import Currency
from utilits.log_settings import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class USD(Currency):
    self.__currency = 'https://minfin.com.ua/ua/currency/usd/'
    self.__usd_retail_json = 'https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json'
    self.__usd_auction_json = 'https://minfin.com.ua/ua/data/currency/auction/usd.1000.median.daily.format.json'
    self.__usd_nbu_json = 'https://minfin.com.ua/data/currency/nbu/nbu.usd.stock.json?1594720251'

    self.__usd_visa = 'https://minfin.com.ua/ua/currency/visa/usd/'
    self.__usd_mastercard = 'https://minfin.com.ua/ua/currency/mastercard/usd/'
    self.__usd_visa_json = 'https://minfin.com.ua/ua/data/currency/card/visa.usd.rates.full.json'
    self.__usd_mastercard_json = 'https://minfin.com.ua/ua/data/currency/card/mc.usd.rates.full.json'
    self.__usd_cards_rates = 'https://minfin.com.ua/ua/data/currency/card/usd.rates.full.json'

    def __init__(self):
        super().__init__()
        log.debug(self.__name__)

    def get_data(self):
        log.debug(self)
        self.__get_usd_retail()

    def __get_usd_retail(self):
        log.debug(self.__currency)

    def __get_usd_auction(self):
        pass

    def __get_usd_nbu(self):
        pass

    def __get_usd_interbank(self):
        pass

    def __get_usd_visa(self):
        pass

    def __get_usd_mastercard(self):
        pass


if __name__ == '__main__':
    usd = USD()
    usd.get_data()

