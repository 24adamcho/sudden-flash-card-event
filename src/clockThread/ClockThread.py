import threading
import json


class ClockThread(threading.Thread):
    __stats__ = {}
    __cards__ = {}
    __period__ = 5 #default seconds between each popup
    __stopflag__ = False
    threadEvent = threading.Event()

    def __init__(self, cardsFile, configFile):
        print("Loading configs and data")

        #check if files exist. if not, throw an error popup and terminate operation


        #load config file for period and other settings
        #load cards file into data
        #load stats file
        print("Configs loaded")

        threading.Thread.__init__(self)
        print("Thread loaded")

    def run(self):
        print("Beginniing thread operation")
        while not self.__stopflag__:
            self.threadEvent.wait(timeout=self.__period__)
            if not self.__stopflag__:
                print("Popup time!")
                self.threadEvent.clear()
        print("ClockThread.run terminated")

    def stop(self):
        self.__stopflag__ = True
        self.threadEvent.set()

        print("Thread operation stopped")

    def getstats(self):
        return self.stats
    