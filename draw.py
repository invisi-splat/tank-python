"""
Defines the drawing process. Call draw() to call the drawing process.
All variables are defined in config.py and can be updated in there.
"""

import config
from config import tank1, tank2
import math


# generation of grids
def generate_grid(gridsize, background, *args, **kwargs):
    """Creates basic grid.

    All grids begin life here!
    """
    formatted_grid = []
    if args:
        background = args[0] + background + config.reset
    for x_unit in range(gridsize[1]):
        formatted_grid_row = []
        for y_unit in range(gridsize[0]):
            formatted_grid_row.append(background)
        formatted_grid.append(formatted_grid_row)
    return formatted_grid


# additions to grids
def layer_grids(back, *grids):
    """Layers the grids passed as parameters.

    The order of the grids defines the drawing order.
    Note that all grids passed must be 2-d grids.
    """
    output = []
    for n in range(len(grids)):
        if n == 0:
            output = grids[n]
        else:
            for m in range(len(grids[n])):  # each 2-d list
                for b in range(len(grids[n][m])):   # each row
                    if grids[n][m][b] == back:
                        pass
                    else:
                        output[m][b] = grids[n][m][b]
    return output


def draw_tanks(grid):
    """Draws the tanks and their respective directional arrows."""
    # Apologies for the spaghetti code!!!!
    x1 = math.floor(tank1.x)
    y1 = math.floor(tank1.y)
    x2 = math.floor(tank2.x)
    y2 = math.floor(tank2.y)
    tank1_coords = ((x1, y1), (x1 + 1, y1), (x1 + 1, y1 + 1), (x1, y1 + 1))
    tank2_coords = ((x2, y2), (x2 + 1, y2), (x2 + 1, y2 + 1), (x2, y2 + 1))
    tank1_arrows = (
                    ((x1, y1 - 1), (x1 + 1, y1 - 1)),
                    ((x1 + 1, y1 - 1), (x1 + 2, y1)),
                    ((x1 + 2, y1), (x1 + 2, y1 + 1)),
                    ((x1 + 2, y1 + 1), (x1 + 1, y1 + 2)),
                    ((x1 + 1, y1 + 2), (x1, y1 + 2)),
                    ((x1, y1 + 2), (x1 - 1, y1 + 1)),
                    ((x1 - 1, y1 + 1), (x1 - 1, y1)),
                    ((x1 - 1, y1), (x1, y1 - 1))
                    )
    tank2_arrows = (
                    ((x2, y2 - 1), (x2 + 1, y2 - 1)),
                    ((x2 + 1, y2 - 1), (x2 + 2, y2)),
                    ((x2 + 2, y2), (x2 + 2, y2 + 1)),
                    ((x2 + 2, y2 + 1), (x2 + 1, y2 + 2)),
                    ((x2 + 1, y2 + 2), (x2, y2 + 2)),
                    ((x2, y2 + 2), (x2 - 1, y2 + 1)),
                    ((x2 - 1, y2 + 1), (x2 - 1, y2)),
                    ((x2 - 1, y2), (x2, y2 - 1))
                    )

    try:
        for pos in range(len(tank1_coords)):
            part = tank1.color[0] + tank1.iteration[0][pos] + config.reset
            grid[tank1_coords[pos][1]][tank1_coords[pos][0]] = part
    except IndexError:
        pass
    try:
        for pos in range(len(tank2_coords)):
            part = tank2.color[0] + tank2.iteration[0][pos] + config.reset
            grid[tank2_coords[pos][1]][tank2_coords[pos][0]] = part
    except IndexError:
        pass

    try:
        pos = int(tank1.direction / 45)
        part0 = tank1.color[0] + tank1.iteration[1][pos % 4][0] + config.reset
        part1 = tank1.color[0] + tank1.iteration[1][pos % 4][1] + config.reset
        grid[tank1_arrows[pos][0][1]][tank1_arrows[pos][0][0]] = part0
        grid[tank1_arrows[pos][1][1]][tank1_arrows[pos][1][0]] = part1
    except IndexError:
        pass

    try:
        pos = int(tank2.direction / 45)
        part0 = tank2.color[0] + tank2.iteration[1][pos % 4][0] + config.reset
        part1 = tank2.color[0] + tank2.iteration[1][pos % 4][1] + config.reset
        grid[tank2_arrows[pos][0][1]][tank2_arrows[pos][0][0]] = part0
        grid[tank2_arrows[pos][1][1]][tank2_arrows[pos][1][0]] = part1
    except IndexError:
        pass

    return grid


def draw_bullets(grid):
    for tank in config.tanklist:
        bullets = tank.bullets
        for bullet in bullets:
            grid[math.floor(bullet.y)][math.floor(bullet.x)] = tank.color[0] \
                                                           + "■" + config.reset
    return grid


def draw_bombs(grid):
    for tank in config.tanklist:
        bombs = tank.bombs
        for bomb in bombs:
            x = math.floor(bomb.x)
            y = math.floor(bomb.y)
            if bomb.explode and bomb.destruct % 2 == 0:  # gives flash
                radius = bomb.radius
                for line in range(len(radius)):
                    currenty = line - math.floor(len(radius) / 2)
                    for currentx in range(radius[line][0], radius[line][1] + 1):
                        grid[y + currenty][x + currentx] = tank.color[1] \
                                                        + " " + config.reset
            else:
                grid[y][x] = tank.color[0] + "◯" + config.reset
    return grid


def surround_with_box(grid, gridsize, boxchars):
    """Surrounds given grid (with assisting gridsize) with box (boxchars)."""
    top_row = boxchars.top_left + boxchars.runs * config.grid[0] \
        + boxchars.top_right
    top_row = list(top_row)
    bottom_row = boxchars.bottom_left + boxchars.runs * config.grid[0] \
        + boxchars.bottom_right
    bottom_row = list(bottom_row)
    grid.insert(0, top_row)
    for row in range(gridsize[1]):
        grid[row + 1].insert(0, boxchars.rises)
        grid[row + 1].append(boxchars.rises)
    grid.append(bottom_row)
    return grid


def append_line_breaks(grid, keeplast=True):
    """Appends line breaks to end of each grid line.

    Set keeplast to be False if final line does not require line break.
    """
    for row in grid:
        row.append("\n")
    if not keeplast:
        del grid[-1][-1]
    return grid


# compilaton of grids
def show(grid):
    """"Flattens" the grid, ready for printing.

    Same effect as .join()ing the grid twice.
    """
    grid = ["".join(row) for row in grid]
    return "".join(grid)


def additions(grid):
    grid = surround_with_box(grid, config.grid, config.BOXCHARS)
    grid = append_line_breaks(grid, False)
    return grid


def create_grid():
    """Puts together all of the grids and the modifications.

    Returns a grid.
    """
    back_grid = generate_grid(config.grid, config.BACKGROUND)
    back_grid = additions(back_grid)
    tank_grid = generate_grid(config.grid, config.BACKGROUND)
    tank_grid = draw_tanks(tank_grid)
    bullet_grid = generate_grid(config.grid, config.BACKGROUND)
    bullet_grid = draw_bullets(bullet_grid)
    bomb_grid = generate_grid(config.grid, config.BACKGROUND)
    bomb_grid = draw_bombs(bomb_grid)
    final_grid = layer_grids(config.BACKGROUND,
                             back_grid, tank_grid, bullet_grid, bomb_grid)
    return final_grid


# global functions
def draw(*args):
    """Main draw function. Call this to display the finalised grid or any other
    things to be drawn.

    Define the variables used in draw.py for the draw() function in config.py.
    """
    try:
        if args[0] == "end" and config.grid[0] > 80:
            for number in str(tank1.score):
                config.score += tank1.color[0] + config.numbers[int(number)] \
                             + config.reset
            config.score += config.dash
            for number in str(tank2.score):
                config.score += tank2.color[0] + config.numbers[int(number)] \
                             + config.reset
            print("\u001b[42;1m" + r"""
      ___                              _        _   
     / __|__ _ _ __  ___   ___ _ _  __| |___ __| |  
    | (_ / _` | '  \/ -_) / -_) ' \/ _` / -_) _` |_ 
     \___\__,_|_|_|_\___| \___|_||_\__,_\___\__,_(_)""" + config.reset)
            print(r"""
  ___                 _
 / __| __ ___ _ _ ___(_)
 \__ \/ _/ _ \ '_/ -_)_
 |___/\__\___/_| \___(_)
            """ + config.score)
        elif args[0] == "end":
            print("Game ended.")
            print(f"Score: {tank1.score} - {tank2.score}")
        elif args[0] == "pause" and config.grid[0] > 60:
            print("\u001b[43;1m" + r"""
       ___                                             _   
      / __|__ _ _ __  ___   _ __  __ _ _  _ ___ ___ __| |  
     | (_ / _` | '  \/ -_) | '_ \/ _` | || (_-</ -_) _` |_ 
      \___\__,_|_|_|_\___| | .__/\__,_|\_,_/__/\___\__,_(_)
                           |_|                             """ + config.reset)
        elif args[0] == "pause":
            print("Game paused.")
        elif args[0] == "flash":
            grid = generate_grid(config.grid, config.BACKGROUND, args[1].color[1])
            grid = surround_with_box(grid, config.grid, config.BOXCHARS)
            print(show(grid))
    except IndexError:
        print(show(create_grid()))
