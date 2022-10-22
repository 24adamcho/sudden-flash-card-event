import tkinter as tk
from tkinter import END, ttk

from popup.QuizLogic import QuizLogic

class PopupWindowFrame(tk.Frame):
    def __init__(self, parent, card, count, splash):
        print("Frame")
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.__count__ = count
        self.__splash__ = splash
        self.__widgets__(card)
        
    def __widgets__(self, card):
        print("frame widgets")
        self.lbl_splash = ttk.Label(self, text=self.__splash__)
        self.lbl_description = tk.Label(self, text=f"(Progress: {self.__count__})(Score:0)", fg='blue')
        self.lbl_card = ttk.Label(self, text = card)
        self.ent_guess = ttk.Entry(self)
        self.lbl_answer = tk.Label(self) #TK ALLOWS FG/BG CONTROL, NOT TTK
        #self.lbl_timer = ttk.Label(self)

        self.lbl_splash.pack()
        self.lbl_description.pack()
        self.lbl_card.pack()
        self.ent_guess.pack()
        self.lbl_answer.pack()
        #self.lbl_timer.pack()

        self.ent_guess.focus_set()
        print("frame widgets packed")

    def getEntryText(self):
        return self.ent_guess.get()

    def correct(self, score):
        self.lbl_answer.config(text="Correct!")
        self.lbl_answer.config(fg="green")
        self.lbl_description.config(text=f"(Progress:{self.__count__})(Score:{score})")
    def incorrect(self, answer):
        self.lbl_answer.config(text=f"Wrong! The answer was [ {answer} ].")
        self.lbl_answer.config(fg="red")

    def nextQuestion(self, card, count, score):
        self.__count__ = count
        self.lbl_description.config(text=f"(Progress:{self.__count__})(Score:{score})")
        self.lbl_answer.config(text="")
        self.lbl_card.config(text=card)
        self.ent_guess.delete(0, END)
    
    #def updateTimer(self, time):
        #self.lbl_timer.config(text=f"Time remaining: {time}")

class PopupWindow(tk.Tk):
    __quizCompleted__ = False

    def __init__(self, ql, splash, options = {"windowSize": "350x100", "popupTimer": 300}):
        print("Initializing window...")
        super().__init__()

        self.title("SUDDEN FLASH CARD EVENT")
        self.__windowSize__ = options["windowSize"]
        self.geometry(self.__windowSize__)

        self.__logic__ = ql
        self.__time__ = options["popupTimer"]
        
        self.bind('<Return>', self.__onNewlineEvent__)
        self.protocol("WM_DELETE_WINDOW", self.__onClose__)
        self.__top__ = self.winfo_toplevel()
        self.__top__.bind("<Unmap>", self.__onUnmap__)

        self.frame = PopupWindowFrame(
            self, 
            self.__logic__.peekCard(),
            self.__logic__.progressStr(),
            splash
            )
        self.frame.pack()
        #self.timerClock()

        #cheese prevention measures
        self.attributes('-topmost',True)
        self.resizable(False, False)
        self.__lockPosition__()
        print("Window initialized")
    
    __flipflop__ = True
    def __onNewlineEvent__(self, event):
        print("Entry submitted")
        if self.__flipflop__: # test answer
            self.__pauseTimer__ = True
            if self.__logic__.guess(self.frame.getEntryText()):
                self.frame.correct(self.__logic__.results()[0])
            else:
                self.frame.incorrect(self.__logic__.peekAnswer())
        else: # next question
            self.__pauseTimer__ = False
            if self.__logic__.nextCard():
                self.frame.nextQuestion(
                    self.__logic__.peekCard(),
                    self.__logic__.progressStr(),
                    self.__logic__.results()[0]
                    )
            else: #no cards available?
                self.__quizCompleted__ = True
                self.noSeriouslyClose() #close window and return score
        self.__flipflop__ = not self.__flipflop__

    def __onClose__(self):
        pass
    def noSeriouslyClose(self):
        print("Window closed!")
        self.destroy()

    def __onUnmap__(self, event):
        self.__top__.wm_deiconify()

    def __lockPosition__(self):
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%s+%d+%d' % (self.__windowSize__, x, y))
        self.after(1, self.__lockPosition__)

    __pauseTimer__ = False
    def timerClock(self):
        if not self.__pauseTimer__:
            m, s = divmod(self.__time__, 60)
            h, m = divmod(m, 60)
            #self.frame.updateTimer(f"{m:02d}:{s:02d}")
            
            self.__time__ -= 1
            if self.__time__ + 1 < 0:
                self.noSeriouslyClose()

        self.after(1000, self.timerClock)

if __name__ == "__main__":
    cards = {
        "test": "answer",
        "mock": "dancer",
        "hole": "water",
        "hell": "water",
        "high": "water"
    }
    #logic = quizlogic.QuizLogic(cards)
    #app = PopupWindow(logic, "You must answer.")
    #app.mainloop()
    print("loop exited")