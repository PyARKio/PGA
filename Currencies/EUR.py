# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from .AbstractCurrency import Currency
from utilits.log_settings import log
from utilits.url_obj import URL


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class EUR(Currency):
    def __init__(self):
        super().__init__()
        log.debug(self)

        self.currency = URL('https://minfin.com.ua/ua/currency/eur/')
        self.retail_json = URL('https://minfin.com.ua/ua/data/currency/retail/eur.rates.full.json')
        self.auction_json = URL('https://minfin.com.ua/ua/data/currency/auction/eur.1000.median.daily.format.json')
        self.nbu_json = URL('https://minfin.com.ua/data/currency/nbu/nbu.eur.stock.json?1594720251')

        self.visa = URL('https://minfin.com.ua/ua/currency/visa/eur/')
        self.mastercard = URL('https://minfin.com.ua/ua/currency/mastercard/eur/')
        self.visa_json = URL('https://minfin.com.ua/ua/data/currency/card/visa.eur.rates.full.json')
        self.mastercard_json = URL('https://minfin.com.ua/ua/data/currency/card/mc.eur.rates.full.json')
        self.cards_rates = URL('https://minfin.com.ua/ua/data/currency/card/eur.rates.full.json')

    def __str__(self):
        return 'Card for EUR'

    def get_data(self):
        log.debug(self)
        self.__get_retail()

    def __get_retail(self):
        log.debug(self.currency)
        if self.currency.status():
            for i, v in self.currency.data.items():
                log.debug(i)
                log.debug(v)
        else:
            for i, v in self.currency.errors.items():
                log.debug(i)
                log.debug(v)

    def __get_auction(self):
        pass

    def __get_nbu(self):
        pass

    def __get_interbank(self):
        pass

    def __get_visa(self):
        pass

    def __get_mastercard(self):
        pass


if __name__ == '__main__':
    eur = EUR()
    eur.get_data()






