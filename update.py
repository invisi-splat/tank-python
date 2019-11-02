"""
Defines the updating process. Call update() to call the updating process.
Updates variables, calculates positions, anything - basically where all the
game logic is written. It's a blank canvas - any code can be written here! This
is essentially where the game really is.
All variables are defined in config.py and can be updated in there.
"""

import config
import shutil
import sys
sys.path.insert(0, r".")
import keyboard


def update_gridsize():
    terminal_size = shutil.get_terminal_size()
    config.GRID = (terminal_size.columns, terminal_size.lines)
    print(config.GRID)


def update():
    """Main update function. Call this to update and calculate. Epic.

    Define the variables used in update.py for the update() function in
    config.py.
    """
    update_gridsize()
