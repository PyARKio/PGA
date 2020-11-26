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

    # NBU *************************************************************************************************

    data_ = press.appeal({'Question to NBU': {'MinFin': {'EUR': 'official_main'}}})
    data_full = data_['Question to NBU']['MinFin']['EUR'][0]
    GrBuild.one_plot_for_bot(Value=[data_full['date'], data_full['official_main']], name='NBU_EUR', sensor_name='NBU EUR')

    data_ = press.appeal({'Question to NBU': {'MinFin': {'USD': 'official_main'}}})
    data_full_nbu = data_['Question to NBU']['MinFin']['USD'][0]
    GrBuild.one_plot_for_bot(Value=[data_full_nbu['date'], data_full_nbu['official_main']], name='NBU_USD', sensor_name='NBU USD')

    # AUCTION **********************************************************************************************

    data_ = press.appeal({'Question to Auction': {'MinFin': {'USD': 'offer_main'}}})
    data_full_auction = data_['Question to Auction']['MinFin']['USD'][0]
    GrBuild.one_plot_for_bot(Value=[data_full_auction['date'], data_full_auction['offer_main']], name='Auction_USD_bid', sensor_name='Auction USD  BiD')

    GrBuild.two_plot_for_bot(Value_1=[data_full_nbu['date'], data_full_nbu['official_main']],
                             Value_2=[data_full_auction['date'], data_full_auction['offer_main']],
                             name='Auction_USD_bid', sensor_name='NBU usd  Auction usd')

    # data_ = press.appeal({'Question to Auction': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to Auction']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Auction_USD_offer', sensor_name='Auction USD  OFFER')
    #
    # data_ = press.appeal({'Question to Auction': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to Auction']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Auction_EUR_bid', sensor_name='Auction EUR  BiD')
    #
    # data_ = press.appeal({'Question to Auction': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to Auction']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Auction_EUR_offer', sensor_name='Auction EUR  OFFER')
    #
    # # BANK **********************************************************************************************
    #
    # data_ = press.appeal({'Question to Bank': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to Bank']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Bank_USD_bid', sensor_name='Bank USD  BiD')
    #
    # data_ = press.appeal({'Question to Bank': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to Bank']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Bank_USD_offer', sensor_name='Bank USD  OFFER')
    #
    # data_ = press.appeal({'Question to Bank': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to Bank']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Bank_EUR_bid', sensor_name='Bank EUR  BiD')
    #
    # data_ = press.appeal({'Question to Bank': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to Bank']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Bank_EUR_offer', sensor_name='Bank EUR  OFFER')
    #
    # # VISA **********************************************************************************************
    #
    # data_ = press.appeal({'Question to Visa': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to Visa']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Visa_USD_bid', sensor_name='Visa USD  BiD')
    #
    # data_ = press.appeal({'Question to Visa': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to Visa']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Visa_USD_offer', sensor_name='Visa USD  OFFER')
    #
    # data_ = press.appeal({'Question to Visa': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to Visa']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Visa_EUR_bid', sensor_name='Visa EUR  BiD')
    #
    # data_ = press.appeal({'Question to Visa': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to Visa']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='Visa_EUR_offer', sensor_name='Visa EUR  OFFER')
    #
    # # MasterCard **********************************************************************************************
    #
    # data_ = press.appeal({'Question to MasterCard': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to MasterCard']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='MasterCard_USD_bid', sensor_name='MasterCard USD  BiD')
    #
    # data_ = press.appeal({'Question to MasterCard': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to MasterCard']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='MasterCard_USD_offer', sensor_name='MasterCard USD  OFFER')
    #
    # data_ = press.appeal({'Question to MasterCard': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to MasterCard']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='MasterCard_EUR_bid', sensor_name='MasterCard EUR  BiD')
    #
    # data_ = press.appeal({'Question to MasterCard': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to MasterCard']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='MasterCard_EUR_offer', sensor_name='MasterCard EUR  OFFER')
    #
    # # InterBank **********************************************************************************************
    #
    # data_ = press.appeal({'Question to InterBank': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to InterBank']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='InterBank_USD_bid', sensor_name='InterBank USD  BiD')
    #
    # data_ = press.appeal({'Question to InterBank': {'MinFin': {'USD': {}}}})
    # data_full = data_['Question to InterBank']['MinFin']['USD']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='InterBank_USD_offer', sensor_name='InterBank USD  OFFER')
    #
    # data_ = press.appeal({'Question to InterBank': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to InterBank']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['bid_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='InterBank_EUR_bid', sensor_name='InterBank EUR  BiD')
    #
    # data_ = press.appeal({'Question to InterBank': {'MinFin': {'EUR': {}}}})
    # data_full = data_['Question to InterBank']['MinFin']['EUR']
    # data_official_main = [[], []]
    # for data in data_full:
    #     data_official_main[0].append(data['time'])
    #     data_official_main[1].append(float(data['offer_main']))
    # GrBuild.one_plot_for_bot(Value=data_official_main, name='InterBank_EUR_offer', sensor_name='InterBank EUR  OFFER')
