import quizlogic

class Popup(object):
    __cards__ = {}

    def __init__(self, cards):
        self.__cards__ = cards
        self.__logic__ = quizlogic.QuizLogic(cards)
        