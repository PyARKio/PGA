# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from AbstractCurrency import Currency
from utilits.log_settings import log
from utilits.url_obj import URL
from utilits.interrupt import Interrupt
from bs4 import BeautifulSoup
import re
from random import randint
from datetime import datetime


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

        # self.__timer = Interrupt(name=self, callback_handler=self.get_data, delay=(30, 67), random_mode=True)
        # self.__timer.go_go()
        # log.info(self.__timer.delay)

        self.__source_one__banks__common = {'time': None, 'value': {'bid': {'main': None, 'diff': None},
                                                                    'offer': {'main': None, 'diff': None},
                                                                    'week': None}}

    @classmethod
    def __str__(cls):
        return 'Card for {}'.format(cls.__name__)

    def get_data(self):
        log.debug(self)
        self.__get_banks()
        self.__get_auction()
        self.__get_nbu()
        # log.info(self.__timer.delay)

    def __get_banks(self):
        if self.__banks.status():
            content = self.__banks.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tbody = div.tbody

            td_bid_offer = tbody.find(class_='mfm-text-nowrap')
            bid_offer = re.findall(r'\S\d{1,2}\.\d{1,3}', td_bid_offer.text)
            td_week = tbody.find(class_='mfcur-sparkline-indicator icon-down-open')
            week = re.findall(r'\S\d{1,2}\.\d{1,3}', td_week.text)

            # https://tproger.ru/translations/regular-expression-python/

            self.__source_one__banks__common['time'] = datetime.now()
            self.__source_one__banks__common['value']['bid']['main'] = bid_offer[0]
            self.__source_one__banks__common['value']['bid']['diff'] = bid_offer[1]
            self.__source_one__banks__common['value']['offer']['main'] = bid_offer[3]
            self.__source_one__banks__common['value']['offer']['diff'] = bid_offer[2]
            self.__source_one__banks__common['value']['week'] = week[0]

            log.info(self.__source_one__banks__common)

    def __get_auction(self):
        if self.__auction.status():
            content = self.__auction.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tbody = div.tbody
            log.info(tbody)

    def __get_nbu(self):
        if self.__nbu.status():
            content = self.__nbu.data['content']
            html = BeautifulSoup(content, 'html.parser')
            main = html.main
            div = main.find(class_='container clearfix')
            tbody = div.tbody
            log.info(tbody)

    def __get_interbank(self):
        pass

    def __get_visa(self):
        pass

    def __get_mastercard(self):
        pass

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


if __name__ == '__main__':
    import time

    usd = USD()
    usd.get_data()
    # while True:
    #     sleep = 1000
    #     time.sleep(sleep)

