# -- coding: utf-8 --
from __future__ import unicode_literals
from random import randint
import threading
import time
from .log_settings import log


__author__ = "PyARKio"
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


def func(data):
    print(data)


# add time of day
class Interrupt(threading.Thread):
    def __init__(self, callback_handler, delay, random_mode=False, name='default_timer'):
        threading.Thread.__init__(self)
        if random_mode and isinstance(delay, tuple):
            self.__delay = randint(delay[0], delay[1])
        elif random_mode and not isinstance(delay, tuple):
            raise AssertionError('You choose random delay. You must get a tuple object in "delay": (from, to)')
        elif not random_mode and isinstance(delay, tuple):
            random_mode = True
            self.__delay = randint(delay[0], delay[1])
        elif not random_mode and not isinstance(delay, int):
            raise AssertionError('delay must be an instance of int object')
        else:
            self.__delay = delay

        self.__name = name
        self.__running = True
        self.__handler = callback_handler
        self.__pause = False
        self.__delay_borders = delay
        self.__random = random_mode

        # self.units = {'callback': self.__handler}

    def __get_delay(self):
        return randint(self.__delay_borders[0], self.__delay_borders[1]) if self.__random else self.__delay

    def pause_enable(self):
        self.__pause = True
        log.info('Pause Enable for {}'.format(self.__name))

    def pause_disable(self):
        self.__pause = False
        log.info('Pause Disable for {}'.format(self.__name))

    def terminate(self):
        self.__pause = True
        self.__running = False
        log.debug('self._running: {}'.format(self.__running))

    def go_go(self):
        self.__running = True
        self.start()
        if self.__pause:
            log.warning('Timer was started, but work in pause mode !')
            return 'Timer was started, but work in pause mode !'
        else:
            return 'Timer was started normally'

    def run(self):
        while self.__running:
            time.sleep(self.__delay)
            if not self.__pause:
                self.__handler()
            self.__delay = self.__get_delay()
        log.info('TIMER STOP !!!')

    @property
    def name(self):
        return self.__name

    @property
    def random_mode(self):
        return self.__random

    @property
    def callback(self):
        return self.__handler

    @property
    def delay(self):
        return self.__delay

    @property
    def delay_borders(self):
        return self.__delay_borders

    def random_mode_enable(self):
        self.__random = True

    def random_mode_disable(self):
        self.__random = False

    def set_callback(self, callback):
        self.__handler = callback

    def set_delay(self, delay):
        self.__delay = delay

    def set_delay_borders(self, borders):
        self.__delay_borders = borders


if __name__ == '__main__':
    i = Interrupt(name='USD', callback_handler=func, delay=(2, 7), random_mode=True)
    i.go_go()
    log.info(i.delay)
    time.sleep(150)
    i.terminate()


