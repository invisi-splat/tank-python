"""
Define config/global variables here to be used in the other modules.
"""

import math  # (surprisingly!)

# framerate
FPS = 20

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

    def __init__(self, startx, starty, direction, speed, power,
                 name, color, controls):  # using "color" for consistency
        self.x = startx       # x and y coords are referring to top left corner
        self.startx = startx  # of tank
        self.y = starty
        self.starty = starty
        self.direction = direction
        self.speed = speed  # units per second
        self.power = power
        self.name = name
        self.color = colors[color]  # ansi escape sequence
        self.controls = controls  # 0 or 1
        self.score = 0
        self.top_left = "┌"
        self.top_right = "┐"
        self.bottom_left = "└"
        self.bottom_right = "┘"
        self.rises = "│"
        self.runs = "─"
        self.iteration = [
                          [self.top_left, self.top_right, self.bottom_right,
                           self.bottom_left],
                          [("/", "\\"), ("─", "│"), ("\\", "/"), ("│", "─")]
                          ]
        self.bullets = []
        self.startd = 0  # directional
        self.starts = 0  # shooting

    def reposition(self):
        self.x = self.startx
        self.y = self.starty

    def check_collision(self, obj):
        collision = {"x": None, "y": None}
        if self.x < 2:
            collision["x"] = -1
        if self.x > obj[0] - 1:
            collision["x"] = 1
        if self.y < 2:
            collision["y"] = -1
        if self.y > obj[1] - 2:
            collision["y"] = 1
        return collision

    def hit_bullet(self):
        x = [math.floor(self.x), math.floor(self.x + 1)]
        y = [math.floor(self.y), math.floor(self.y + 1)]
        for bullet in allbullets:
            bulletx = math.floor(bullet.x)
            bullety = math.floor(bullet.y)
            if bullet.invins <= 0:
                if ((x[0] == bulletx or x[1] == bulletx)
                    and (y[0] == bullety or y[1] == bullety)):
                    return True
            else:
                bullet.invins -= 1  # invinsibility frames
        return False

    def shoot_bullet(self):
        self.bullets.append(Bullet(self.x, self.y, self.direction, self.power,
                                   self.name))


tank1 = Tank(10, 10, 0, 3, 0.25, "Tank 1", "Red", 0)
tank2 = Tank(20, 10, 0, 3, 0.25, "Tank 2", "Blue", 1)

tanklist = [tank1, tank2]
allbullets = []

"""
For reference:
Black: \u001b[30m
Red: \u001b[31m
Green: \u001b[32m
Yellow: \u001b[33m
Blue: \u001b[34m
Magenta: \u001b[35m
Cyan: \u001b[36m
White: \u001b[37m
Reset: \u001b[0m
In order to make it bright, add ;1 in between the [x and the "m".
"""


class Bullet:
    def __init__(self, startx, starty, direction, speed, origin):
        self.x = startx
        self.startx = startx
        self.y = starty
        self.starty = starty
        self.direction = direction
        self.speed = speed
        self.origin = origin
        self.invins = 8  # invinsibility frames - i.e. cannot hurt tanks
        self.life = 360  # length of bullet life in frames


quit = False  # whether game has been quit or not
pause = False  # whether game has been paused or not
gamemode = 0  # gamemode - 0: game, 1: menu, 2: settings
# measuring cooldown
# directional:
cooldown1 = 0.2
# shooting:
cooldown2 = 0.2
