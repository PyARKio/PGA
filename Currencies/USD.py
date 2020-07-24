# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from .AbstractCurrency import Currency
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
import re
from random import randint


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class USD(Currency):
    Currency = '-/-'
    Retail = '-/-'
    Auction = '-/-'
    NBU = '-/-'
    Visa = '-/-'
    MasterCard = '-/-'

    def __init__(self):
        super().__init__()
        log.debug(self)

        self.__currency = URL('https://minfin.com.ua/ua/currency/usd/')
        self.__banks = URL('https://minfin.com.ua/ua/currency/banks/usd/')
        self.__auction = URL('https://minfin.com.ua/ua/currency/auction/usd/buy/all/')
        self.__nbu = URL('https://minfin.com.ua/ua/currency/nbu/usd/')
        self.__retail_json = URL('https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json')
        self.__auction_json = URL('https://minfin.com.ua/ua/data/currency/auction/usd.1000.median.daily.format.json')
        self.__nbu_json = URL('https://minfin.com.ua/data/currency/nbu/nbu.usd.stock.json?1594720251')

        self.__visa = URL('https://minfin.com.ua/ua/currency/visa/usd/')
        self.__mastercard = URL('https://minfin.com.ua/ua/currency/mastercard/usd/')
        self.__visa_json = URL('https://minfin.com.ua/ua/data/currency/card/visa.usd.rates.full.json')
        self.__mastercard_json = URL('https://minfin.com.ua/ua/data/currency/card/mc.usd.rates.full.json')
        self.__cards_rates = URL('https://minfin.com.ua/ua/data/currency/card/usd.rates.full.json')

    @classmethod
    def __str__(cls):
        return 'Card for {}'.format(cls.__name__)

    def get_data(self):
        log.debug(self)
        self.__get_retail()

    def __get_retail(self):
        log.debug(self.__currency)
        if self.__currency.status():
            content = self.__currency.data['content']
            # log.info(content)

            html = BeautifulSoup(content, 'html.parser')

            # [$] Курс долара до гривні на 07.07.2020 в Україні ᐈ Мінфін
            # try:
            #     log.info('\n{}'.format(html.title.text))
            # except Exception as err:
            #     log.error(err)

            # log.info('{}\n'.format('*' * 50))
            main = html.main

            div = main.findAll(class_='mfz-container')

            # get active currency value
            div_mfm_grey_bg = div[1].find(class_='mfm-grey-bg')
            div_mfm_grey_bg_tbody = div_mfm_grey_bg.find('tbody')
            tr = div_mfm_grey_bg_tbody.findAll('tr')
            log.info(len(tr))

            if len(tr) == 2:
                # Auction
                tds = tr[0].findAll('td')
                USD.Auction = {'bid': tds[1].text.replace('\n', ''),
                               'offer': tds[2].text.replace('\n', ''),
                               'week': tds[3].text.replace('\n', '')}
                log.info(USD.Auction)

                # NBU
                tds = tr[1].findAll('td')
                USD.NBU = {'nbu': tds[1].text.replace('\n', ''),
                           'week': tds[2].text.replace('\n', '')}
                log.info(USD.NBU)

            elif len(tr) == 3:
                # Retail
                tds = tr[0].findAll('td')
                USD.Retail = {'bid': tds[1].text.replace('\n', ''),
                               'offer': tds[2].text.replace('\n', ''),
                               'week': tds[3].text.replace('\n', '')}
                log.info(USD.Retail)

                # Auction
                tds = tr[1].findAll('td')
                USD.Auction = {'bid': tds[1].text.replace('\n', ''),
                               'offer': tds[2].text.replace('\n', ''),
                               'week': tds[3].text.replace('\n', '')}
                log.info(USD.Auction)

                # NBU
                tds = tr[2].findAll('td')
                USD.NBU = {'nbu': tds[1].text.replace('\n', ''),
                           'week': tds[2].text.replace('\n', '')}
                log.info(USD.NBU)

            # for i, v in self.__currency.data.items():
            #     log.debug(i)
            #     log.debug(v)
        else:
            for i, v in self.__currency.errors.items():
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
    import time

    usd = USD()
    while True:
        usd.get_data()
        sleep = randint(265, 1378)
        log.info(sleep)
        log.info('\n')
        time.sleep(sleep)

