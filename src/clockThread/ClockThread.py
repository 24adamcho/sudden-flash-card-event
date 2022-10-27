import random
import threading

from popup.Popup import Popup

class ClockThread(threading.Thread):
    __stats__ = {}
    __cards__ = {}
    __config__ = {}
    __period__ = 5 #default seconds between each popup
    __stopflag__ = False
    threadEvent = threading.Event()

    def __init__(self, config, stats, cards, periodSeconds, splashes):
        print("Loading configs and data")

        self.__config__ = config
        self.__stats__ = stats
        self.__cards__ = cards
        self.__period__ = periodSeconds
        self.__splashes__ = splashes

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
                questionCount = self.__config__["popupQuestionCount"]
                if len(adaptedpool) < questionCount:
                    questionCount = len(adaptedpool)

                pool = random.sample(adaptedpool, k=questionCount)
                
                if self.__config__["randomCardInversion"]: #invert if config toggled
                    for i in range(len(pool)):
                            if random.getrandbits(1):
                                pool[i] = (pool[i][0], pool[i][1])
                            else:
                                pool[i] = (pool[i][1], pool[i][0]) #invert tuple access
                
                eligableForUpgrade = False
                if self.__config__["adaptiveCardPool"] and pool.count(adaptedpool[cardMaxCount - 1]) > 0:
                    eligableForUpgrade = True

                #for i in range(self.__config__["popupQuestionCount"]): #select a few random cards
                #    k = random.choice(adaptedpool)
                #    if self.__config__["randomCardInversion"]: #invert if config toggled
                #        if random.getrandbits(1):
                #            pool.append((k[0], k[1]))
                #        else:
                #            pool.append((k[1], k[0])) #invert tuple access
                #    else:
                #        pool.append((k[0], k[1]))
                random.shuffle(pool)

                splash = random.choice(self.__splashes__)

                #popup
                p = Popup(pool, splash, self.__config__)
                p.trigger()
                #thread continues after p terminates
                results = p.results()
                self.__stats__["score"] += results[0]
                if results[1]: ##if FC
                    self.__stats__["fc"] += 1
                    if eligableForUpgrade:
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
    