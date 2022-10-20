from email import message
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import QuizLogic

class PopupWindow(tk.Tk):
    __quizCompleted__ = False

    def __init__(self, cards, quizlogic, options = {"windowSize":"300x300"}):
        print("Initializing window...")
        super().__init__()

        self.title("SUDDEN FLASH CARD EVENT")
        self.geometry(options["windowSize"]) #TODO add windowSize to cfg.json

        self.lbl_description = ttk.Label(self, text="You must answer.")
        self.lbl_card = tk.Label()
        self.ent_guess = tk.Entry()
        self.lbl_answer = tk.Label()
        
        def onNewlineEvent(event):
            print("Entry submitted")
        self.bind('<Return>', onNewlineEvent)

        def onClose(event):
            print("Window closed!")
            self.destroy()
        self.protocol("WM_DELETE_WINDOW", onClose)

        self.lbl_description.pack()
        self.lbl_card.pack()
        self.ent_guess.pack()
        self.lbl_answer.pack()
        
        print("Window initialized")

if __name__ == "main":
    PopupWindow("", "").mainloop()