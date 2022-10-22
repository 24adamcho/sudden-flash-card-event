import codecs
import json
import sys
from infi.systray import SysTrayIcon

from clockThread.ClockThread import ClockThread

class TrayMenu(object):
    def __init__(self, configFile):
        print("opening system tray")
        self.__configFile__ = configFile
        self.__clockThread__ = self.__loadClockThread__()
        
        menu = (
            ("Refresh card pack", None, self.refreshClock),
            #("Snooze", None, self.snooze),
            #("Time until next surprise:", None, lambda self:{})
        )
        self.systray = SysTrayIcon(
            None, 
            "Sudden Flash Card Event interface", 
            menu,
            on_quit=self.__onQuitCallback__
        )

        self.__clockThread__.start()
        self.systray.start()
        print("tray opened.")

        ##timer removed because of logic conflicts + inducing anxiety is better for learning
    #    self.__t__ = self.__config__["timerSeconds"]
    #    self.__timerCallback__()

    #def __timerCallback__(self):
    #    self.__t__ -= 1
    #    if self.__t__ < 0:
    #        self.__t__ = self.__config__["timerSeconds"]
    #    m, s = divmod(self.__t__, 60)
    #    h, m = divmod(m, 60)
    #    self.systray.update(hover_text=f"Sudden Flash Card Event in: {m:02d}:{s:02d}")
    #    timerThread = threading.Timer(1, self.__timerCallback__)
    #    timerThread.start()

    def __loadClockThread__(self):
        print("Loading config files...")
        def loadJson(file):
            #check if files exist. if not, throw an error popup and terminate operation
            try:
                print("attempting to open file")
                f = codecs.open(file, mode='r', encoding='utf-8')
                print("converting file to json")
                dict = json.loads(f.read().encode('utf-8'))
                print("dumped!")
                print(json.dumps(dict, indent=4, ensure_ascii=False))
                print("closing file...")
                f.close()
            except:
                sys.exit(f"Error in loading ${file}")
            return dict

        #load config file for other file locations
        self.__config__ = loadJson(self.__configFile__)
        #load stats file
        stats = loadJson(self.__config__["statsFile"])
        #load cards file into data
        cards = loadJson(self.__config__["cardFile"])
        #load splash file
        splashes = loadJson(self.__config__["splashFile"])

        period = self.__config__["timerSeconds"]
        print("Configs loaded")

        return ClockThread(self.__config__, stats, cards, period, splashes)

    def refreshClock(self, systray):
        self.__clockThread__.stop()
        self.__clockThread__ = self.__loadClockThread__()
        self.__clockThread__.start()
        pass

    def snooze(self, systray):
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
            print("Stats saved to " + self.__config__["statsFile"])
        except:
            print("Unable to save stats to file")
        pass

if __name__ == "__main__":
    tray = TrayMenu("omegalul")
    print("test")