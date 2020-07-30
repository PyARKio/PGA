# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from BasisForCurrencies.AbstractCurrency import Currency
from utilits.log_settings import log
from utilits.url_obj import URL
from bs4 import BeautifulSoup
from utilits.interrupt import Interrupt
from random import randint
from Currencies.USD_Utilits.Bank import Bank
from Currencies.USD_Utilits.Auction import Auction
from Currencies.USD_Utilits.NBU import NBU
from Currencies.USD_Utilits.InterBank import InterBank
from Currencies.USD_Utilits.Visa import Visa
from Currencies.USD_Utilits.MasterCard import MasterCard


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

        self.__retail_json = URL('https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json')
        self.__auction_json = URL('https://minfin.com.ua/ua/data/currency/auction/usd.1000.median.daily.format.json')
        self.__nbu_json = URL('https://minfin.com.ua/data/currency/nbu/nbu.usd.stock.json?1594720251')

        self.__visa_json = URL('https://minfin.com.ua/ua/data/currency/card/visa.usd.rates.full.json')
        self.__mastercard_json = URL('https://minfin.com.ua/ua/data/currency/card/mc.usd.rates.full.json')
        self.__cards_rates = URL('https://minfin.com.ua/ua/data/currency/card/usd.rates.full.json')

        # self.__timer = Interrupt(name=self, callback_handler=self.get_data, delay=(30, 67), random_mode=True)
        # self.__timer.go_go()
        # log.info(self.__timer.delay)

        # WARNING    \S\d{1,2}\.\d{1,3} ['27.550', '0.050', '0.000', '27.800']
        self.__bank = Bank('https://minfin.com.ua/ua/currency/banks/usd/')
        self.__auction = Auction('https://minfin.com.ua/ua/currency/usd/')
        self.__nbu = NBU('https://minfin.com.ua/ua/currency/nbu/usd/')
        self.__interbank = InterBank('https://minfin.com.ua/ua/currency/mb/')
        self.__visa = Visa('https://minfin.com.ua/ua/currency/visa/usd/')
        self.__mastercard = MasterCard('https://minfin.com.ua/ua/currency/mastercard/usd/')

    @classmethod
    def __str__(cls):
        return 'Card for {}'.format(cls.__name__)

    # WARNING    \S\d{1,2}\.\d{1,3} ['27.550', '0.050', '0.000', '27.800']
    def get_data(self):
        log.info(self.__bank.get)
        log.info(self.__bank)

        log.info(self.__auction.get)
        log.info(self.__auction)

        log.info(self.__nbu.get)
        log.info(self.__nbu)

        log.info(self.__interbank.get)
        log.info(self.__interbank)

        log.info(self.__visa.get)
        log.info(self.__visa)

        log.info(self.__mastercard.get)
        log.info(self.__mastercard)

    def __artifact(self):
        log.debug(self.__currency)
        if self.__currency.status():
            content = self.__currency.data['content']
            html = BeautifulSoup(content, 'html.parser')
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

