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


def update_gridsize(snap):
    """Updates the size of the grid.

    If "snap" is passed as a parameter, then the grid changes size dynamically.
    """
    if snap == "snap":
        terminal_size = shutil.get_terminal_size()
        # lines = 3 because of the 2 occupied by the box and the 1 occupied by
        # the cursor
        config.lines_to_delete = terminal_size.lines
        config.grid = (terminal_size.columns - 2, terminal_size.lines - 3)
    else:
        config.lines_to_delete = config.grid[1]


def check_keypress(keyboard_event):
    return keyboard_event.name


def pause():
    config.pause = True


def quit():
    config.quit = True


def update():
    """Main update function. Call this to update and calculate. Epic.

    Define the variables used in update.py for the update() function in
    config.py.
    """
    update_gridsize("snap")
