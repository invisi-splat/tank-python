"""
Define config/global variables here to be used in the other modules.
"""

# alter cooldown period between refreshes for testing purposes
TEST_COOLDOWN = 10

# here we call the area in which the game is set the "grid"
GRID = (10, 10)  # (x, y) - x across, y down
BACKGROUND = " "  # background to the grid. must be a char

lines_to_delete = 1  # lines to delete in delete.py


# box drawing chars for the grid
class Box:
    def __init__(self):
        self.top_left = "╔"
        self.top_right = "╗"
        self.bottom_left = "╚"
        self.bottom_right = "╝"
        self.rises = "║"
        self.runs = "═"


BOXCHARS = Box()
