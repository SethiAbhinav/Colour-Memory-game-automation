# Colour-Memory-game-automation
**Automating the colour memory game. A project I completed on 12th of June, 2021.**



# Requirements:


```
pyautogui       --> Locating objects on screen
time            --> Delay
keyboard        --> Exit program 
win32, win32con --> Faster clicking than pyautogui
```

# Python:
```python
import pyautogui
import keyboard
import time,win32api,win32con
```

**Game url:** https://www.coolmathgames.com/0-color-memory#immersiveModa

# How the game works:
This is a memory game wherein you have to remember the sequence of colours shown to you by the game. You have to repeat the pattern once the sequence is over.

# Project Details:
I had always wanted to learn how bots were made for games, and thus I started with a simpler game (in my opinion).

**Process:**
- I wanted a way by which the computer can "see" the colour being flashed and store it in memory. It should also be able to realise when the sequence is over and it is it's turn to repeat what it "saw".
- Thus, I used the pyautogui library to look at the center of each colour and kept checking when it wasn't the colour it was supposed to be ( i.e, when it flashes white).
- Once, I have identified the colour I store it in a list as 1, 2, 3 or 4 corresponding to yellow, red , blue and green, respectively.

**Problems faced:**
- Since the bot was too fast it would register a flash as 4 or 5 flashes and thus I had to add a delay to counter this.
- The bot was "seeing" all the time and thus, when it was clicking as well, it took the colours it clicked as a sequence shown by the game. To deal with this, I added a control variable which would act as a flag to let it know when to take input and when not to. 

**After project thoughts:**
- The bot is perfect, it can go on forever (unless my system runs out of memory ofcourse xD).

