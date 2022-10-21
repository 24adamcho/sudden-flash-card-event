import random
import threading
from popup.popup import Popup

class ClockThread(threading.Thread):
    __stats__ = {}
    __cards__ = {}
    __config__ = {}
    __period__ = 5 #default seconds between each popup
    __stopflag__ = False
    threadEvent = threading.Event()

    def __init__(self, config, stats, cards, periodSeconds):
        print("Loading configs and data")

        self.__config__ = config
        self.__stats__ = stats
        self.__cards__ = cards
        self.__period__ = periodSeconds

        threading.Thread.__init__(self)
        print("Thread loaded")

    def run(self):
        print("Beginning thread operation")
        waitTime = self.__period__
        while not self.__stopflag__:
            self.threadEvent.wait(timeout=waitTime)
            if not self.__stopflag__:
                print("Popup time!")

                #randomly pick from card pool
                if self.__config__["adaptiveCardPool"]:
                    cardMaxCount = self.__stats__["adaptiveCardPoolSize"]
                else:
                    cardMaxCount = len(self.__cards__)

                pool = list(self.__cards__.items())[:cardMaxCount] ##subset of cards below cardMaxCount
                popuppool = {}
                for i in range(self.__config__["popupQuestionCount"]): #select a few random cards
                    k = random.choice(pool)
                    if self.__config__["randomCardInversion"]: #invert if bit set
                        if random.getrandbits(1):
                            popuppool[k] = self.__cards__[k]
                        else:
                            popuppool[self.__cards__[k]] = k
                    else:
                        popuppool[k] = self.__cards__[k]
                random.shuffle(popuppool)

                #popup
                p = Popup(popuppool, "splash", self.__config__)
                p.trigger()
                #thread continues after p terminates
                results = p.results()
                self.__stats__["score"] += results[0]
                if results[1]: ##if FC
                    self.__stats__["adaptiveCardPoolSize"] += 1
                    if self.__config__["adaptiveTimer"]:
                        waitTime = self.__period__ + self.__config__["adaptiveTimerBonus"]
                else:
                    waitTime = self.__period__

                self.threadEvent.clear()
        print("ClockThread.run terminated")

    def stop(self):
        self.__stopflag__ = True
        self.threadEvent.set()

        print("Thread operation stopped")

    def snooze(self, t):
        self.threadEvent.wait(timeout=t)

    def getstats(self):
        return self.__stats__
    