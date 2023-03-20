# marvel-snap-afk-farm

A python script using pyautogui and opencv to afk farm in marvel snap (preferably using Agatha)

# How it works

The script uses `pyautogui` to click on different buttons of the game.
This works with either steam version or an app that emulated the game (like bluestacks).
Every second it takes a screenshot of your game and checks through a list of possible buttons to click (like play, end turn, collect rewards etc.). They can be found in the resources folder.
We grayscale the screenshot of the game and the screenshots of the button and then use `opencv` for template matching. 
Once we found a match the `pyautogui` library moves the mouse on the given x/y coordonates and perfroms a mouse click.

## Playing cards

This does not play any cards for you! 
It works best with an agatha deck since she will do all the plays and the bot can just end turn and re-queue once the game is done.

# How to use

Make sure you have python installed (it has been tested with version 3.10)
Make sure you have git installed

```bash
# Clone this repository
$ git clone https://github.com/isvora/marvel-snap-afk-farm

# Install dependencies
$ pip install -r requirements.txt

# Edit the screenshots if needed
In the resources folder you have screenshots from different in game buttons (play, end turn etc.)
You can retake those with any tool and replace them to match your resolution.

# Run the bot
$ pyton main.py
```bash

# Disclaimer

I'm not responsible for anything that might happen to your account if you use this bot. 
You are not breaking any rules as the bot just mimics what a human would do, but still use it at your own risk.
