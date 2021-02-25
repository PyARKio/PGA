# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.AuctionDepartment import Auction
from InstituteForCurrency.Departments.BankDepartment import Bank
from InstituteForCurrency.Departments.InterBankDepartment import InterBank
from InstituteForCurrency.Departments.NBUCurrencyDepartment import NBU
from InstituteForCurrency.Departments.MasterCardDepartment import MasterCard
from InstituteForCurrency.Departments.VisaDepartment import Visa
from Arsenal.Chronometer import Chronometer
from Arsenal.Chronicler import log
import datetime
from Arsenal import GrBuild


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class PressCentre:
    def __init__(self):
        self.__chronometer = Chronometer()
        self.__chronometer.start()

        self.__auction = Auction(chrono=self.__chronometer)
        self.__bank = Bank(chrono=self.__chronometer)
        self.__inter_bank = InterBank(chrono=self.__chronometer)
        self.__nbu = NBU(chrono=self.__chronometer)
        self.__visa = Visa(chrono=self.__chronometer)
        self.__mastercard = MasterCard(chrono=self.__chronometer)

        self.__departments = {'Question to Auction': self.__auction.question,
                              'Question to Bank': self.__bank.question,
                              'Question to InterBank': self.__inter_bank.question,
                              'Question to NBU': self.__nbu.question,
                              'Question to Visa': self.__visa.question,
                              'Question to MasterCard': self.__mastercard.question}

    def appeal(self, letter):
        answer_to_user = {}
        for key, value in letter.items():
            log.info('')
            log.info('Key: {}'.format(key))
            log.info('Value: {}'.format(value))
            if self.__departments.get(key):
                answer_to_user[key] = self.__departments[key](value)
        return answer_to_user


if __name__ == '__main__':
    press = PressCentre()

    # # NBU *************************************************************************************************
    #
    # data_ = press.appeal({'Question to NBU': {'MinFin': {'EUR': 'official_main'}}})
    # data_full = data_['Question to NBU']['MinFin']['EUR'][0]
    # GrBuild.one_plot_for_bot(Value=[data_full['date'], data_full['official_main']], name='NBU_EUR', sensor_name='NBU EUR')
    #
    # data_ = press.appeal({'Question to NBU': {'MinFin': {'USD': 'official_main'}}})
    # data_full_nbu = data_['Question to NBU']['MinFin']['USD'][0]
    # GrBuild.one_plot_for_bot(Value=[data_full_nbu['date'], data_full_nbu['official_main']], name='NBU_USD', sensor_name='NBU USD')
    #
    # # AUCTION **********************************************************************************************
    #
    data_ = press.appeal({'Question to Auction': {'MinFin': {'USD': 'offer_main'}}})
    data_full_auction_offer = data_['Question to Auction']['MinFin']['USD'][0]
    GrBuild.one_plot_for_bot(Value=[data_full_auction_offer['date'], data_full_auction_offer['offer_main']], name='Auction_USD_offer', sensor_name='Auction USD  Offer')
    #
    # GrBuild.two_plot_for_bot(Value_1=[data_full_nbu['date'], data_full_nbu['official_main']],
    #                          Value_2=[data_full_auction_offer['date'], data_full_auction_offer['offer_main']],
    #                          yLabel_1='USD', yLabel_2='USD',
    #                          name='NBU_USD_Auction_USD_offer', sensor_name='NBU usd  Auction usd')
    #
    data_ = press.appeal({'Question to Auction': {'MinFin': {'USD': 'bid_main'}}})
    data_full_auction_bid = data_['Question to Auction']['MinFin']['USD'][0]
    GrBuild.one_plot_for_bot(Value=[data_full_auction_bid['date'], data_full_auction_bid['bid_main']], name='Auction_USD_bid', sensor_name='Auction USD  BiD')
    #
    # GrBuild.two_plot_for_bot(Value_1=[data_full_auction_bid['date'], data_full_auction_bid['bid_main']],
    #                          Value_2=[data_full_auction_offer['date'], data_full_auction_offer['offer_main']],
    #                          yLabel_1='USD', yLabel_2='USD',
    #                          name='Auction_USD_bid_offer', sensor_name='BID  OFFER')
    #
    # data_ = press.appeal({'Question to Auction': {'MinFin': {'EUR': {}}}})
    #
    # # BANK **********************************************************************************************
    #
    # data_ = press.appeal({'Question to Bank': {'MinFin': {'USD': {}}}})
    #
    # data_ = press.appeal({'Question to Bank': {'MinFin': {'EUR': {}}}})
    #
    # # VISA **********************************************************************************************
    #
    # data_ = press.appeal({'Question to Visa': {'MinFin': {'USD': {}}}})
    #
    # data_ = press.appeal({'Question to Visa': {'MinFin': {'EUR': {}}}})
    #
    # # MasterCard **********************************************************************************************
    #
    # data_ = press.appeal({'Question to MasterCard': {'MinFin': {'USD': {}}}})
    #
    # data_ = press.appeal({'Question to MasterCard': {'MinFin': {'EUR': {}}}})
    #
    # # InterBank **********************************************************************************************
    #
    # data_ = press.appeal({'Question to InterBank': {'MinFin': {'USD': {}}}})
    #
    # data_ = press.appeal({'Question to InterBank': {'MinFin': {'EUR': {}}}})
