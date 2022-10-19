# Class flow and specifications
### Individual subsections
##### Popup
```mermaid
classDiagram
direction LR
    class Logic{
        -cards
        +init(cards)
        +guess(card) bool
        +results() stats
    }
    class Window{
        window stuff
        +init(Logic)
        +trigger()
        +hide()
    }
    class Popup{
        -Window
        -Logic
        +init(cards)
        +trigger() stats
    }

    Popup <|-- Window
    Window <|-- Logic
    Popup <|-- Logic
```
##### Clock daemon
```mermaid
classDiagram
direction LR
    class Clock{
        +period
        +sleepme(seconds)
    }
    class ClockDaemon{
        -Popup
        +init(String cardsFile)
        +start()
        +getstats() stats
        +stop()
    }
    class Data{
        +Cards
        +Stats
    }

    ClockDaemon <|-- Data
    ClockDaemon <|-- Clock
```

##### Desktop app
```mermaid
classDiagram
direction LR
    class TrayMenu{
        -ClockDaemon
        +quit()
        +refreshFileList()
        +changeDaemonCards()
        +openFileDirectory()
        +snooze()
    }
```

### Full diagram
```mermaid
classDiagram
direction TB
    class Logic{
        -cards
        +init(cards)
        +guess(card) bool
        +results() stats
    }
    class Window{
        window stuff
        +init(Logic)
        +trigger()
        +hide()
    }
    class Popup{
        -Window
        -Logic
        +init(cards)
        +trigger() stats
    }

    class Clock{
        +period
        +sleepme(seconds)
    }
    class ClockDaemon{
        -Popup
        +init(String cardsFile)
        +start()
        +getstats() stats
        +stop()
    }
    class Data{
        +Cards
        +Stats
    }

    class TrayMenu{
        +quit()
        +refreshFileList()
        +changeDaemonCards()
        +openFileDirectory()
        +snooze()
    }

    Popup <|-- Window
    Window <|-- Logic
    Popup <|-- Logic

    ClockDaemon <|-- Data
    ClockDaemon <|-- Clock

    ClockDaemon <|-- Popup
    TrayMenu <|-- ClockDaemon
```
