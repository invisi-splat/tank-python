"""
Main process. Run this program to start the game.
"""

import update
import draw
import delete
import config
import keyboard


def prepare():
    keyboard.add_hotkey("space+p", update.pause)
    keyboard.add_hotkey("space+q", update.quit)


def mainloop():
    while True:
        update.update()
        draw.draw()
        delete.delete()
        if config.quit:
            draw.draw("end")
            break
        elif config.pause:
            draw.draw("pause")
            keyboard.wait("space+p")
            config.pause = False


prepare()
mainloop()
