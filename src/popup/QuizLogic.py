

class QuizLogic(object):
    __cards__ = {}

    def __init__(self, cardKeys, cards):
        self.__cards__ = cards
        self.__guessIndex__ = 0
        self.__score__ = 0
        self.__cardKeys__ = cardKeys

    # guess the card's answer
    #   returns:
    #       True - answer is correct
    #              increments score
    #       False - answer was incorrect
    def guess(self, guess):
        if guess == self.peekAnswer():
            self.__score__ += 1
            output = True
        else:
            output = False
        print(f"Score: {self.__score__}")
        return output    

    # next Card increments the card counter
    #   returns:
    #       True - if the current index is valid
    #       False - if the current index is out of bounds
    def nextCard(self):
        self.__guessIndex__ += 1
        if self.__guessIndex__ >= len(self.__cards__):
            return False
        return True

    def results(self):
        return [self.__score__, self.__score__ == len(self.__cards__)]

    def peekAnswer(self):
        return self.__cards__[self.__cardKeys__[self.__guessIndex__]]
    def peekCard(self):
        return self.__cardKeys__[self.__guessIndex__]

    def progressStr(self):
        return str(self.__guessIndex__ + 1) + "/" + str(len(self.__cards__))