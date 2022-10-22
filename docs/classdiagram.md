# Class flow and specifications
### Individual subsections
##### Popup
```mermaid
classDiagram
direction LR
    class QuizLogic{
        -cards : list
        -guessIndex : int
        -score : int

        +init(cards : list)
        +guess(card : str) bool
        +nextCard() bool
        +results() list (score : int, fc : bool)
        +peekCard() str
        +peekAnswer() str
        +progressSrt() str
    }
    class PopupWindow{
        window stuff
        -logic : QuizLogic
        -top : tk.topLevelWindow
        -frame : PopupWindowFrame
        -windowSize : str

        +init(ql : QuizLogic, splash : str, options : dict)
        -onNewlineEvent() //update frame
        -onClose() //refuse close
        -onUnmap() //refuse minimize
        +noSeriouslyClose() //actually close
        -lockPosition()
    }
    class PopupWindowFrame{
        -count : str
        -splash : str

        -lbl_description
        -lbl_card
        -ent_guess
        -lbl_answer
        -widgets(card)

        +getEntryText()
        +correct(score)
        +incorrect(answer)
        +nextQuestion(card, count, score)
    }
    class Popup{
        -cards : list
        -logic : QuizLogic
        -app : PopupWindow
        +init(cards : list, splash : str, options : dict)
        +trigger()
        +results() logic.results()
    }

    Popup <|-- PopupWindow
    PopupWindow <|-- PopupWindowFrame
    PopupWindow <|-- QuizLogic
    Popup <|-- QuizLogic
```
##### Clock thread
```mermaid
classDiagram
direction LR
    class ClockThread{
        -stats : dict
        -cards : dict
        -config : dict
        -period : int
        -stopflag : bool
        -popup : Popup
        +threadEvent
        
        +init(String cardsFile)
        +run()
        +stop()
        +snooze(t) //NOT WORKING, UNUSED
        +getstats() stats
    }
```

##### Desktop app
```mermaid
classDiagram
direction LR
    class TrayMenu{
        -clockThread : ClockThread
        -config : dict
        -configFile : str
        -systray : infi.systray.SysTrayIcon

        -loadClockThread() ClockThread
        -loadJson(file) dict
        +quit()
        +refreshClock(systray)
        +snooze(systray) //NOT WORKING, UNUSED
    }
```

### Full diagram
```mermaid
classDiagram
direction LR
    class QuizLogic{
        -cards : list
        -guessIndex : int
        -score : int

        +init(cards : list)
        +guess(card : str) bool
        +nextCard() bool
        +results() list (score : int, fc : bool)
        +peekCard() str
        +peekAnswer() str
        +progressSrt() str
    }
    class PopupWindow{
        window stuff
        -logic : QuizLogic
        -top : tk.topLevelWindow
        -frame : PopupWindowFrame
        -windowSize : str

        +init(ql : QuizLogic, splash : str, options : dict)
        -onNewlineEvent() //update frame
        -onClose() //refuse close
        -onUnmap() //refuse minimize
        +noSeriouslyClose() //actually close
        -lockPosition()
    }
    class PopupWindowFrame{
        -count : str
        -splash : str

        -lbl_description
        -lbl_card
        -ent_guess
        -lbl_answer
        -widgets(card)

        +getEntryText()
        +correct(score)
        +incorrect(answer)
        +nextQuestion(card, count, score)
    }
    class Popup{
        -cards : list
        -logic : QuizLogic
        -app : PopupWindow
        +init(cards : list, splash : str, options : dict)
        +trigger()
        +results() logic.results()
    }

    class ClockThread{
        -stats : dict
        -cards : dict
        -config : dict
        -period : int
        -stopflag : bool
        -popup : Popup
        +threadEvent
        
        +init(String cardsFile)
        +run()
        +stop()
        +snooze(t) //NOT WORKING, UNUSED
        +getstats() stats
    }

    class TrayMenu{
        -clockThread : ClockThread
        -config : dict
        -configFile : str
        -systray : infi.systray.SysTrayIcon

        -loadClockThread() ClockThread
        -loadJson(file) dict
        +quit()
        +refreshClock(systray)
        +snooze(systray) //NOT WORKING, UNUSED
    }

    Popup <|-- PopupWindow
    PopupWindow <|-- PopupWindowFrame
    PopupWindow <|-- QuizLogic
    Popup <|-- QuizLogic

    ClockThread<|-- Popup
    TrayMenu <|-- ClockThread
```
