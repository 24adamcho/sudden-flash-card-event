import json
import os
import sys
from infi.systray import SysTrayIcon

import clockThread.clockthread

class TrayMenu(object):
    def __init__(self, configFile):
        self.__config__ = configFile
        self.__clockThread__ = self.__loadClockThread__()
        
        menu = (
            ("Refresh card pack", None, self.refreshClock),
            ("Snooze", None, self.snooze)
        )
        self.systray = SysTrayIcon(
            None, 
            "Sudden Flash Card Event interface", 
            menu,
            on_quit=self.__onQuitCallback__
        )

        self.__clockThread__.start()
        self.systray.start()

    def __loadClockThread__(self):
        def loadJson(file):
            #check if files exist. if not, throw an error popup and terminate operation
            if os.path.exists(file):
                f = open(file)
                dict = json.loads(f)
                f.close()
            else:
                sys.exit(f"Error in loading ${file}")
            return dict

        #load config file for other file locations
        config = loadJson("../config/cfg.json")
        #load stats file
        stats = loadJson(self.__config__["statsFile"])
        #load cards file into data
        cards = loadJson(self.__config__["cardFile"])

        period = self.__config__["timerSeconds"]
        print("Configs loaded")

        return clockThread.clockthread.ClockThread(config, stats, cards, period)

    def refreshClock(self):
        self.__clockThread__.stop()
        self.__clockThread__ = self.__loadClockThread__()
        self.__clockThread__.start()
        pass

    def snooze(self):
        self.__clockThread__.snooze(self.__config__["snoozeTime"])
        pass

    def __onQuitCallback__(self, systray):
        self.__clockThread__.stop()
        self.__clockThread__.join()

        #save stats to file
        try:
            f = open(self.__config__["statsFile"], "w")
            f.write(json.dumps(self.__clockThread__.getstats(), indent=4))
            f.close()
        except:
            print("Unable to save stats to file")
        pass

if __name__ == "__main__":
    tray = TrayMenu("omegalul")
    print("test")