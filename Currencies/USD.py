# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from AbstractCurrency import Currency
from utilits.log_settings import log
from utilits.url_obj import URL


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class USD(Currency):
    Currency = None
    Retail = None
    Auction = None
    NBU = None
    Visa = None
    MasterCard = None

    def __init__(self):
        super().__init__()
        log.debug(self)

        self.__currency = URL('https://minfin.com.ua/ua/currency/usd/')
        self.__retail_json = URL('https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json')
        self.__auction_json = URL('https://minfin.com.ua/ua/data/currency/auction/usd.1000.median.daily.format.json')
        self.__nbu_json = URL('https://minfin.com.ua/data/currency/nbu/nbu.usd.stock.json?1594720251')

        self.__visa = URL('https://minfin.com.ua/ua/currency/visa/usd/')
        self.__mastercard = URL('https://minfin.com.ua/ua/currency/mastercard/usd/')
        self.__visa_json = URL('https://minfin.com.ua/ua/data/currency/card/visa.usd.rates.full.json')
        self.__mastercard_json = URL('https://minfin.com.ua/ua/data/currency/card/mc.usd.rates.full.json')
        self.__cards_rates = URL('https://minfin.com.ua/ua/data/currency/card/usd.rates.full.json')

    def __str__(self):
        return 'Card for USD'

    def get_data(self):
        log.debug(self)
        self.__get_usd_retail()

    def __get_usd_retail(self):
        log.debug(self.__currency)
        if self.__currency.status():
            for i, v in self.__currency.data.items():
                log.debug(i)
                log.debug(v)
        else:
            for i, v in self.__currency.errors.items():
                log.debug(i)
                log.debug(v)

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

