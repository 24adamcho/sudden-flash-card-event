import random
import threading

from popup import popup

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

                adaptedpool = list(self.__cards__.items())[:cardMaxCount] ##subset of cards below cardMaxCount
                pool = []
                for i in range(self.__config__["popupQuestionCount"]): #select a few random cards
                    k = random.choice(adaptedpool)
                    if self.__config__["randomCardInversion"]: #invert if config toggled
                        if random.getrandbits(1):
                            pool.append(k)
                        else:
                            pool.append((k[1], k[0])) #invert tuple access
                    else:
                        pool.append(k)
                random.shuffle(pool)

                #popup
                p = popup.Popup(pool, "splash", self.__config__)
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
    