"""
Main process. Run this program to start the game.
"""

from update import update
from draw import draw
from delete import delete
import config
import time


def mainloop():
    while True:
        update()
        draw()
        delete()
        time.sleep(config.TEST_COOLDOWN)


mainloop()
