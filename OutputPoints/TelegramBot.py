# -- coding: utf-8 --
from __future__ import unicode_literals
# from configs import token
import telebot
from Currencies import USD
from time import sleep


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


bot = telebot.TeleBot('1369528104:AAEgqxtJ_X0gYqnEuI06BFSJ7QTlKbOPJs0')
usd = USD.USD()


@bot.message_handler()
def else_request(message):
    USD.log.info('\n')
    USD.log.info(message.chat.id)
    USD.log.info(message.text)
    USD.log.info('\n')

    if message.chat.id == 681970459 or message.chat.id == 663891547:
        usd.get_data()
        bot.send_message(message.chat.id, 'Retail: {}\nAuction: {}\nNBU: {}'.format(USD.USD.Retail,
                                                                                    USD.USD.Auction,
                                                                                    USD.USD.NBU))
    else:
        bot.send_message(681970459, 'NEW USER: {}\nREQUEST: {}'.format(message.chat.id, message.text))


def telegram_bot__run():
    while True:
        try:
            bot.polling()
        except Exception as err:
            USD.log.error(err)
        else:
            sleep(5)


if __name__ == '__main__':
    telegram_bot__run()




