import QuizLogic

class Popup(object):
    __cards__ = {}

    def __init__(self, cards):
        self.__cards__ = cards
        self.__logic__ = QuizLogic.QuizLogic(cards)
        