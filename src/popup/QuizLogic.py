

class QuizLogic(object):
    __cards__ = {}

    def __init__(self, cards):
        self.__cards__ = cards
        self.__guessIndex__ = 0
        self.__score__ = 0

    def guess(self, card):
        if card == self.peekAnswer():
            output = True
        else:
            output = False
        self.__guessIndex__ += 1
        return output

    def results(self):
        return self.__score__

    def peekAnswer(self):
        return self.__cards__.values()[self.__guessIndex__]
    def peekCard(self):
        return self.__cards__.keys()[self.__guessIndex__]