

class QuizLogic(object):
    __cards__ = {}

    def __init__(self, cards):
        self.__cards__ = cards
        self.__guessIndex__ = 0
        self.__score__ = 0

    def guess(self, card):
        if card == self.__cards__.keys()[self.__guessIndex__]:
            return True
        else:
            return False

    def incrementGuess(self):
        self.__guessIndex__+= 1

    def flushValues(self):
        self.__guessIndex__ = 0
        self.__score__ = 0

    def results(self):
        return self.__score__