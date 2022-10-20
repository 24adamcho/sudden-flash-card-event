import sys
import threading
import json
import os.path

class ClockThread(threading.Thread):
    __stats__ = {}
    __cards__ = {}
    __config__ = {}
    __period__ = 5 #default seconds between each popup
    __stopflag__ = False
    threadEvent = threading.Event()

    def __init__(self, configFile):
        print("Loading configs and data")

        def loadJson(file, dict):
            #check if files exist. if not, throw an error popup and terminate operation
            if os.path.exists(file):
                f = open(file)
                dict = json.loads(f)
                f.close()
            else:
                sys.exit(f"Error in loading ${file}")

        #load config file for other file locations
        loadJson("../config/cfg.json", self.__config__)
        #load stats file
        loadJson(self.__config__["statsFile"], self.__stats__)
        #load cards file into data
        loadJson(self.__config__["cardFile"], self.__cards__)
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

        #save stats to file
        try:
            f = open(self.__config__["statsFile"], "w")
            f.write(json.dumps(self.__stats__, indend=4))
            f.close()
        except:
            print("Unable to save stats to file")

        print("Thread operation stopped")

    def getstats(self):
        return self.stats
    