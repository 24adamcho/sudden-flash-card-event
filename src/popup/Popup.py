import threading
from time import sleep

import quizlogic
import popupwindow

class Popup(object):
    def __init__(self, cards, splash, options = {"windowSize": "350x100", "timer": 60}):
        self.__cards__ = cards
        self.__logic__ = quizlogic.QuizLogic(cards)
        self.__timer__ = options["timer"]
        self.__app__ = popupwindow.PopupWindow(self.__logic__, splash, options)

    def trigger(self):
        self.__app__.mainloop()
        print("loop cancelled")

    def results(self):
        return self.__logic__.results()

if __name__ == "__main__":
    cards = {
        "test": "answer",
        #"mock": "dancer",
        #"hole": "water",
        #"hell": "water",
        #"high": "water"
    }
    #Popup(cards, "You must answer.").trigger()
    pass
    #Popup(cards, "dgjseztae").trigger()
    pass