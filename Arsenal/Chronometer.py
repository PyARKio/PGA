# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
import threading
from time import sleep


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Chronometer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__kvant = 60
        self.__run = True
        self.__current_mark = 0
        self.__clock_face = {}
        for i in range(0, 60):
            self.__clock_face[i] = []

    def run(self):
        while self.__run:
            sleep(self.__kvant)
            for callback in self.__clock_face[self.__current_mark]:
                log.info(callback)
                callback()

            self.__clock_face[self.__current_mark] = []
            if self.__current_mark == 59:
                self.__current_mark = 0
            else:
                self.__current_mark += 1

    def change_kvant(self, kvant):
        self.__kvant = kvant

    def add_marks(self, whom, mark):
        self.__clock_face[mark['Position']].append(mark['CallBack'])
        log.info(self.__clock_face)
        log.info(whom)

    def terminate(self, whom):
        log.info(whom)
        self.__run = False


if __name__ == '__main__':
    chrono = Chronometer()







