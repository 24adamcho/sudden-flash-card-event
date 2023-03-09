# Sudden Flash Card Event

## Description 
Sudden Flash Card Event is a language study tool that interrupts whatever the user is doing and displays a popup quiz of random flashcards.

## Installation
This program is built for python 3.10.4 on Windows. 
This program also uses the library [infi.systray]("https://github.com/Infinidat/infi.systray"). Install it with:
```
pip install infi.systray
```
or run 
```
make setup
```

## Usage
To run, use `run.bat`:
```batch
start "Sudden Flash Card Event" pythonw ./src/main.pyw --config "./config/cfg.json"
```
or
```
make run
```
You cannot kill the quiz window. There is no escape for you.

#### Configuration

The default configuration files are in `config/config.json`. Here are the configuration settings:
| Key                   | Default Value                 | Description                        
| --------------------- | ---------------------         | ---------------------------------- 
| `statsFile`           | `./config/stats.json`         | Directory to the stats file to use 
| `cardFile`            | `./config/cards/default.json` | Directory for the card pack to use 
| `splashFile`          | `./config/splashes.json`      | Directory of taunting messages     
| `adaptiveCardPool`    | `true`                        | Changes the card pool size based on stat performance. If false, the entire card pool will be used.
| `timerSeconds`        | `900` (15 minutes)            | Time between popups, in seconds
| `popupQuestionCount`  | `10`                          | Questions in each popup quiz
| `windowSize`          | `350x100`                     | Size of popup window
| `popupTimer`          | `300` (5 minutes)             | Unused
| `adaptiveTimer`       | `true`                        | Whether or not to change time between popups based on previous quiz performance. If false, no bonus will be added.
| `adaptiveTimerBonus`  | `300` (5 minutes)             | Bonus time to add if the previous quiz was perfectly done, in seconds
| `randomCardInversion` | `true`                        | Randomly reverse cards
| `snoozeTime`          | `300` (5 minutes)             | Unused
| `font`                | `arial`                       | Font for popup text
| `fontSize`            | `30`                          | Font size for popup text; make sure `windowSize` is large enough to display all of it!

Some user statistics are available in `config/stats.json`:
| Key                       | Default Value | Description   
| ------------------------- | ------------- | -----------
| `adaptiveCardPoolSize`    | `5`           | Max index of adaptive card pool, if `adaptiveCardPool` is set to true. Not recommended to go too far below `popupQuestionCount`, or there will be a large amount of repeated cards
| `score`                   | `0`           | Compounding value of how many questions the user has gotten right. Vanity value.
| `fc`                   | `0`           | Compounding value of how many quizzes the user has gotten perfect. Vanity value.

`config/splashes.json` is a list of taunting messages. Please put whatever you want to insult yourself with in there.

`config/cards/default.json` shows an example of how to build a flash card pack, formatted like so:
| Key       | Value 
| --------- | -----------
| card face | card answer
