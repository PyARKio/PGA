# -- coding: utf-8 --
from __future__ import unicode_literals
from utilits.log_settings import log
import threading
import time


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Chronometer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__clock_face = {}
        for i in range(1, 60):
            self.__clock_face[i] = []




if __name__ == '__main__':
    chrono = Chronometer()







