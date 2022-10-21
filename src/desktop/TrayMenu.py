from infi.systray import SysTrayIcon

class TrayMenu(object):
    def __init__(self, clockthread):
        self.__clockThread__ = clockthread
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

        self.systray.start()

    def refreshClock(self):
        pass

    def snooze(self):
        pass

    def __onQuitCallback__(self, systray):
        pass

if __name__ == "__main__":
    tray = TrayMenu("omegalul")
    print("test")