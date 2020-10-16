# -- coding: utf-8 --
from __future__ import unicode_literals
from .VisaSources.VisaMinFin.Curator import MinFinCurator
from Arsenal.Chronicler import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Visa:
    def __init__(self, chrono):
        self.__minfin = MinFinCurator(chrono)
        # self.__kurs = KursCurator(chrono)
        # self.__finance = FinanceCurator(chrono)

        self.__curators = {'MinFin': self.__minfin.question_to_curator,
                           # 'Kurs': self.__minfin.question_to_curator,
                           # 'Finance': self.__minfin.question_to_curator
                           }

    def answer(self):
        ...

    def question(self, question):
        answer_to_press_centre = {}
        for key, value in question.items():
            answer_to_press_centre[key] = self.__curators[key](value)
        return answer_to_press_centre
