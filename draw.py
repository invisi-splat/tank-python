"""
Defines the drawing process. Call draw() to call the drawing process.
All variables are defined in config.py and can be updated in there.
"""

import config
from config import tank1, tank2


# generation of grids
def generate_grid(gridsize, background, *args, **kwargs):
    """Creates basic grid.

    All grids begin life here!
    """
    formatted_grid = []
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
    x1 = tank1.x
    y1 = tank1.y
    x2 = tank2.x
    y2 = tank2.y
    tank1_coords = ((x1, y1), (x1 + 1, y1), (x1 + 1, y1 + 1), (x1, y1 + 1))
    tank2_coords = ((x2, y2), (x2 + 1, y2), (x2 + 1, y2 + 1), (x2, y2 + 1))

    for pos in range(len(tank1_coords)):
        colored_part = tank1.color + tank1.iteration[pos] + config.reset
        grid[tank1_coords[pos][1]][tank1_coords[pos][0]] = colored_part
    for pos in range(len(tank2_coords)):
        colored_part = tank2.color + tank2.iteration[pos] + config.reset
        grid[tank2_coords[pos][1]][tank2_coords[pos][0]] = colored_part

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
    final_grid = layer_grids(config.BACKGROUND, back_grid, tank_grid)
    return final_grid


def draw(*args):
    """Main draw function. Call this to display the finalised grid or any other
    things to be drawn.

    Define the variables used in draw.py for the draw() function in config.py.
    """
    try:
        if args[0] == "end" and config.grid[0] > 60:
            print(r"""
      ___                              _        _
     / __|__ _ _ __  ___   ___ _ _  __| |___ __| |
    | (_ / _` | '  \/ -_) / -_) ' \/ _` / -_) _` |_
     \___\__,_|_|_|_\___| \___|_||_\__,_\___\__,_(_)
                """)
        elif args[0] == "end":
            print("Game ended.")
        elif args[0] == "pause" and config.grid[0] > 60:
            print(r"""
       ___                                             _
      / __|__ _ _ __  ___   _ __  __ _ _  _ ___ ___ __| |
     | (_ / _` | '  \/ -_) | '_ \/ _` | || (_-</ -_) _` |_
      \___\__,_|_|_|_\___| | .__/\__,_|\_,_/__/\___\__,_(_)
                           |_|
            """)
        elif args[0] == "pause":
            print("Game paused.")
    except IndexError:
        print(show(create_grid()))
