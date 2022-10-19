import threading
import time

class ClockThread(threading.Thread):
    stats = {}
    data = {}

    def __init__(self, cardsFile, configFile):
        print("Initializing Clock daemon...")

    def run(self):
        print("Daemon started")

    def stop(self):
        print("Daemon stopped")

    def getstats(self):
        return self.stats

    