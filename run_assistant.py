# -- coding: utf-8 --
from __future__ import unicode_literals
from utilits.log_settings import log
from MinFin import minfin_parser
# from OutputPoints import TelegramBot
import configs


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


if __name__ == '__main__':
    # TelegramBot.telegram_bot__run()

    soup = minfin_parser.request_to_minfin(url=configs.usd_currency)
    minfin_parser.get_usd_currency(soup=soup)

