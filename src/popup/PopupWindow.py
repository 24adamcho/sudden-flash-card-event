import tkinter as tk
from tkinter import ttk

import quizlogic

class PopupWindow(tk.Tk):
    __quizCompleted__ = False

    def __init__(self, cards, quizlogic, options = {"windowSize":"300x300"}):
        print("Initializing window...")
        super().__init__()

        self.title("SUDDEN FLASH CARD EVENT")
        self.geometry(options["windowSize"]) #TODO add windowSize to cfg.json

        self.__logic__ = quizlogic.QuizLogic()

        self.lbl_description = ttk.Label(self, text="You must answer.")
        self.lbl_card = ttk.Label()
        self.ent_guess = ttk.Entry()
        self.lbl_answer = ttk.Label()
        
        self.bind('<Return>', self.onNewlineEvent)
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.lbl_description.pack()
        self.lbl_card.pack()
        self.ent_guess.pack()
        self.lbl_answer.pack()
        
        print("Window initialized")
    
    def onNewlineEvent(self, event):
        print("Entry submitted")

    def onClose(self):
        print("Window closed!")
        self.destroy()

if __name__ == "__main__":
    app = PopupWindow("", "")
    app.mainloop()