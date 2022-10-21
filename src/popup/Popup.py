import threading
from time import sleep

import popup.QuizLogic
import popup.PopupWindow

class Popup(object):
    def __init__(self, cards, splash, options = {"windowSize": "350x100", "popupTimer": 60}):
        self.__cards__ = cards
        self.__logic__ = popup.QuizLogic.QuizLogic(cards)
        self.__timer__ = options["popupTimer"]
        self.__app__ = popup.PopupWindow.PopupWindow(self.__logic__, splash, options)

    def trigger(self):
        self.__app__.mainloop()
        print("loop cancelled")

    def results(self):
        return self.__logic__.results()

if __name__ == "__main__":
    cards = [
        ("test", "answer"),
        ("mock", "dancer"),
        ("hole", "water"),
        ("hell", "water"),
        ("high", "water")
    ]
    Popup(cards, "You must answer.").trigger()
    pass
    #Popup(cards, "dgjseztae").trigger()
    pass