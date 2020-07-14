# -- coding: utf-8 --
from __future__ import unicode_literals
from configs import token
import telebot


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


bot = telebot.TeleBot(token)


@bot.message_handler()
def else_request(message):
    bot.send_message(message.chat.id, '!')


def telegram_bot__run():
    bot.polling()


