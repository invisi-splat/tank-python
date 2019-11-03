"""
Main process. Run this program to start the game.
"""

import update
import draw
import delete
import config
import time
import keyboard


def prepare():
    keyboard.add_hotkey("space+p", update.pause)
    keyboard.add_hotkey("space+q", update.quit)
    keyboard.on_press(update.check_keypress)


def mainloop():
    while True:
        update.update()
        draw.draw()
        delete.delete()
        time.sleep(config.TEST_COOLDOWN)
        if config.quit:
            draw.draw("end")
            break
        elif config.pause:
            draw.draw("pause")
            keyboard.wait("space+p")
            config.pause = False


prepare()
mainloop()
