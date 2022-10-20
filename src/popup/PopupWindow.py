import tkinter as tk
from tkinter import ttk

import quizlogic

class PopupWindowFrame(tk.Frame):
    def __init__(self, parent, card, answer):
        print("Frame")
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.__card__ = card
        self.__answer__ = answer
        self.widgets()
        
    def widgets(self):
        print("frame widgets")
        self.lbl_description = ttk.Label(self, text="You must answer.")
        self.lbl_card = ttk.Label(self, text = self.__card__)
        self.ent_guess = ttk.Entry(self)
        self.lbl_answer = tk.Label(self) #TK ALLOWS FG/BG CONTROL, NOT TTK

        self.lbl_description.pack()
        self.lbl_card.pack()
        self.ent_guess.pack()
        self.lbl_answer.pack()
        print("frame widgets packed")

    def getEntryText(self):
        return self.ent_guess.get()

    def correct(self):
        self.lbl_answer.config(text="Correct!")
        self.lbl_answer.config(fg="green")
    def incorrect(self):
        self.lbl_answer.config(text=f"Wrong! The answer was [ {self.__answer__} ].")
        self.lbl_answer.config(fg="red")

class PopupWindow(tk.Tk):
    __quizCompleted__ = False

    def __init__(self, cards, ql, options = {"windowSize":"350x100"}):
        print("Initializing window...")
        super().__init__()

        self.title("SUDDEN FLASH CARD EVENT")
        self.geometry(options["windowSize"]) #TODO add windowSize to cfg.json

        self.__logic__ = quizlogic.QuizLogic(cards)
        
        self.bind('<Return>', self.onNewlineEvent)
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.frames = list()
        for card, answer in cards.items():
            self.frames.append(PopupWindowFrame(self, card, answer))

        self.frame = PopupWindowFrame(self, "test", "water")

        self.frame.pack()
        
        print("Window initialized")
    
    def onNewlineEvent(self, event):
        print("Entry submitted")
        if self.__logic__.guess(self.frame.getEntryText()):
            self.frame.correct()
        else:
            self.frame.incorrect()
        
        if self.__logic__.nextCard():
            pass #change to next frame
        else:
            self.onClose() #close window and return score

    def onClose(self):
        print("Window closed!")
        self.destroy()

if __name__ == "__main__":
    cards = {
        "test": "answer",
        "mock": "dancer"
    }
    logic = quizlogic.QuizLogic(cards)
    app = PopupWindow(cards, logic)
    app.mainloop()
    print("loop exited")