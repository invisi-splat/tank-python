"""
Define config/global variables here to be used in the other modules.
"""

# alter cooldown period between refreshes for testing purposes
TEST_COOLDOWN = 0

# here we call the area in which the game is set the "grid"
grid = (10, 10)  # (x, y) - x across, y down
BACKGROUND = " "  # background to the grid. must be a char

lines_to_delete = grid[1]  # lines to delete in delete.py

colors = {"Red": "\u001b[31;1m", "Blue": "\u001b[34;1m"}
reset = "\u001b[0m"

# box drawing chars for the grid
class Boxchars:
    """Box drawing characters for the surrounding box."""

    def __init__(self):
        self.top_left = "╔"
        self.top_right = "╗"
        self.bottom_left = "╚"
        self.bottom_right = "╝"
        self.rises = "║"
        self.runs = "═"


BOXCHARS = Boxchars()


class Tank:
    """Tank class. Each tank object is an instantiation of this class.

    Initialise with its starting x and y coords, its direction (a bearing), its
    speed, its name, its color and its controls (either 0 or 1).
    """

    def __init__(self, startx, starty, direction, speed,
                 name, color, controls):  # using "color" for consistency
        self.x = startx       # x and y coords are referring to top left corner
        self.startx = startx  # of tank
        self.y = starty
        self.starty = starty
        self.direction = direction
        self.speed = speed
        self.name = name
        self.color = colors[color]
        self.controls = controls
        self.top_left = "┌"
        self.top_right = "┐"
        self.bottom_left = "└"
        self.bottom_right = "┘"
        self.rises = "│"
        self.runs = "─"
        self.iteration = [self.top_left, self.top_right, self.bottom_right,
                          self.bottom_left]

    def reposition(self):
        self.x = self.startx
        self.y = self.starty


tank1 = Tank(10, 10, 0, 5, "Tank 1", "Red", 0)
tank2 = Tank(20, 10, 0, 5, "Tank 2", "Blue", 1)

quit = False  # whether game has been quit or not
pause = False  # whether game has been paused or not
