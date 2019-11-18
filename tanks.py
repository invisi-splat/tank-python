"""
Main process. Run this program to start the game.
"""

import update
import draw
import delete
import config
import sys
import getpass
sys.path.insert(0, r".")
import keyboard


def prepare():
    keyboard.add_hotkey("space+p", update.pause)
    keyboard.add_hotkey("space+q", update.quit)


def mainloop():
    update.initupdate()
    draw.draw()
    delete.delete()
    while True:
        update.update()
        draw.draw()
        delete.delete()
        if config.quit:
            draw.draw("end")
            getpass.getpass("")
            break
        elif config.pause:
            draw.draw("pause")
            keyboard.wait("space+p")
            config.pause = False


prepare()
mainloop()
