"""
Defines the drawing process. Call draw() to call the drawing process.
Draws the grid (area in which the game is set - the viewing window) and menus,
scores, etc... everything to be shown, really. Some basic code is here in order
to assist with the process.
All variables are defined in config.py and can be updated in there.
"""

import config


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


def surround_with_box(grid, gridsize, box):
    """Surrounds given grid (with assisting gridsize) with box (boxchars)."""
    top_row = box.top_left + box.runs * config.grid[0] + box.top_right
    top_row = list(top_row)
    bottom_row = box.bottom_left + box.runs * config.grid[0] + box.bottom_right
    bottom_row = list(bottom_row)
    grid.insert(0, top_row)
    for row in range(gridsize[1]):
        grid[row + 1].insert(0, box.rises)
        grid[row + 1].append(box.rises)
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


def additions(grid, *args, **kwargs):
    grid = surround_with_box(grid, config.grid, config.BOXCHARS)
    grid = append_line_breaks(grid, False)
    return grid


def create_grid():
    """Puts together all of the grids and the modifications.

    Returns a grid.
    """
    formatted_grid = generate_grid(config.grid, config.BACKGROUND)
    modified_grid = additions(formatted_grid)
    return modified_grid


def draw():
    """Main draw function. Call this to display the finalised grid or any other
    things to be drawn.

    Define the variables used in draw.py for the draw() function in config.py.
    """
    print(show(create_grid()))
