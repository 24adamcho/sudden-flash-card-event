import threading
from time import sleep

import quizlogic
import popupwindow

class Popup(object):
    def __init__(self, cards, splash, options = {"windowSize": "350x100", "timer": 5}):
        self.__cards__ = cards
        self.__logic__ = quizlogic.QuizLogic(cards)
        self.__timer__ = options["timer"]
        self.__app__ = popupwindow.PopupWindow(self.__logic__, splash, options)

    def trigger(self):
        t = threading.Timer(self.__timer__, self.__app__.noSeriouslyClose)
        t.start()
        #while not self.__app__.closeme:
        #    self.__app__.update()
        #print("loop exited")
        #self.__app__.destroy()
        self.__app__.mainloop()
        print("loop cancelled")
        if not t.finished.is_set():
            t.cancel()
            print("timer cancelled")
        t.join()
        print("timer rejoined main thread")

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
    app = Popup(cards, "You must answer.")
    app.trigger()
    sleep(3)
    bapp = Popup(cards, "dgjseztae")
    bapp.trigger()
    sleep(3)